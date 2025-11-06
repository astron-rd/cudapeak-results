#!/usr/bin/env python3

import dataframe_image as dfi
import json
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import os
import pandas as pd
import re
from typing import List, Optional

# Constants
ROW_ORDER = [
    "fp32",
    "mma_tf32_16_16_8",
    "mma_bf16_16_16_16",
    "mma_f16_16_16_16",
    "mma_e4m3_16_8_32",
    "mma_e5m2_16_8_32",
    "mma_s8_16_8_32",
    "mma_s8_16_16_16",
    "mma_e2m1_16_8_64",
    "mma_e3m2_16_8_32",
    "mma_s4_8_8_32",
    "bmma_b1_8_8_128_and",
    "bmma_b1_8_8_128_xor",
    "bmma_b1_16_8_256_and",
    "bmma_b1_16_8_256_xor",
]


def parse_filename(filename: str) -> tuple:
    """Extract architecture, GPU, benchmark, and comment from filename."""
    match = re.match(r"^(\w*)-(\w*)-(\w*)(?:-(\w*))?", filename)
    if match:
        return match.groups()
    return None, None, None, None


def load_json_data(filename: str) -> Optional[dict]:
    """Load and parse JSON data from file."""
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Failed to parse {filename}: {e}")
        return None


def process_benchmark_data(
    data: list, arch: str, gpu: str, bench: str, comment: str
) -> pd.DataFrame:
    """Process benchmark data into a structured DataFrame."""
    # Device info from first record
    device_info = pd.DataFrame.from_records(data[:1])

    # Benchmark results from remaining records
    benchmark_data = pd.DataFrame.from_records(data[1:])
    benchmark_data = (
        benchmark_data.sort_values(["name", "runtime"])
        .drop_duplicates("name", keep="first")
        .reset_index(drop=True)
    )

    # Add metadata columns
    benchmark_data["arch"] = arch
    benchmark_data["gpu"] = f"{arch.capitalize()} {gpu}"
    benchmark_data["bench"] = bench
    benchmark_data["comment"] = comment
    benchmark_data["mp_count"] = device_info["multi_processor_count"][0]

    max_frequency = device_info["clock_rate"][0] * 1000
    benchmark_data["max_frequency"] = max_frequency

    return benchmark_data


def parse_file(filename: str) -> Optional[pd.DataFrame]:
    """Parse a benchmark file and return processed DataFrame."""
    arch, gpu, bench, comment = parse_filename(filename)
    if not all([arch, gpu, bench]):
        return None

    data = load_json_data(filename)
    if data is None:
        return None

    return process_benchmark_data(data, arch, gpu, bench, comment)


def compute_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """Compute derived metrics like OPs per cycle and normalized performance."""
    df = df.copy()

    # Fallback to max_frequency if frequency is NaN
    df["frequency"] = df["frequency"].fillna(df["max_frequency"])

    # Compute operations per cycle
    df["ops_per_cycle"] = df.tops / (df.mp_count * df.frequency * 1e-3)

    # Scale measured TOPS to max frequency
    df["max_tops"] = df.tops / df.frequency * df.max_frequency

    # Normalize by slowest benchmark per GPU
    df["normalized_ops"] = df["ops_per_cycle"] / df.groupby("gpu")[
        "ops_per_cycle"
    ].transform(lambda x: x.min())

    return df


def create_styled_table(
    df: pd.DataFrame,
    value_col: str,
    row_order: List[str],
    column_order: Optional[List[str]] = None,
) -> pd.DataFrame:
    """Create a styled table with consistent formatting."""
    # Create pivot table
    table = (
        df.pivot_table(index="name", columns="gpu", values=value_col)
        .fillna(0)
        .reindex(row_order)
    )

    # Sort columns by first row values
    if column_order is None:
        column_order = table.iloc[0].sort_values(ascending=True).index
    table = table[column_order]

    # Style function for hiding zeros
    def hide_nan(x):
        return f"color: {mcolors.rgb2hex(plt.cm.Greens(0.0))}" if x == 0 else ""

    # Apply styling
    styled = (
        table.style.background_gradient(cmap="Greens").format("{:.2f}").map(hide_nan)
    )

    return table, styled, column_order


def generate_report(table_absolute, table_normalized) -> str:
    """Generate the markdown report content."""
    return f"""
# CUDA Peak Performance Report

This auto-generated report presents benchmark results for the [cudapeak](https://github.com/astron-rd/cudapeak) FP32 and MMA synthetic performance benchmarks on various GPUs.

The benchmarks evaluate synthetic workloads designed to measure peak operations per second (OPs), providing insights into architectural efficiency and computational limits.

## Absolute Performance
Measured in teraoperations per second (TOPs), showing raw computational throughput for various data types and MMA sizes.

![Absolute Performance](performance_absolute.png)

<details>
<summary><b>📊 Data Table</b></summary>
{table_absolute.to_html()}
</details>

## Normalized Performance  
Scaled relative to each GPU's slowest individual benchmark result, revealing how performance scales across different data types.

![Normalized Performance](performance_normalized.png)

<details>
<summary><b>📊 Data Table</b></summary>
{table_normalized.to_html()}
</details>

*Report generated on {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M UTC')}*
"""


def main():
    """Main execution function."""
    # Combine all JSON files into one dataframe
    dfs = []
    for filename in os.listdir():
        if filename.endswith(".json"):
            df = parse_file(filename)
            if df is not None:
                dfs.append(df)

    if not dfs:
        print("No valid JSON files found!")
        return

    df = pd.concat(dfs, ignore_index=True)

    # Filter out rows with comments (e.g., 'turbo')
    if "comment" in df.columns:
        df = df[df["comment"].isna()].drop(columns=["comment"])

    # Compute metrics
    df = compute_metrics(df)

    # Create styled tables
    table_absolute, table_absolute_styled, column_order = create_styled_table(
        df, "max_tops", ROW_ORDER
    )
    table_normalized, table_normalized_styled, _ = create_styled_table(
        df, "normalized_ops", ROW_ORDER, column_order
    )

    # Export styled tables as images
    dfi.export(table_absolute_styled, "performance_absolute.png")
    dfi.export(table_normalized_styled, "performance_normalized.png")

    # Generate and save report
    report_content = generate_report(table_absolute, table_normalized)

    with open("README.md", "w") as f:
        f.write(report_content)

    print("Report generated successfully as README.md")


if __name__ == "__main__":
    main()

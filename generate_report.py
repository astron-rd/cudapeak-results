#!/usr/bin/env python3

import dataframe_image as dfi
import json
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import os
import pandas as pd
import re
from PIL import Image
from typing import List, Optional, Tuple

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

TCGEN05_ROW_ORDER = [
    "tcgen05_tf32_128_128_32",
    "tcgen05_bf16_128_128_64",
    "tcgen05_f16_128_128_64",
    "tcgen05_e4m3_128_128_128",
    "tcgen05_e5m2_128_128_128",
    "tcgen05_s8_128_128_128",
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
    """Compute derived metrics like OPs per cycle."""
    df = df.copy()

    # Fallback to max_frequency if frequency is NaN
    df["frequency"] = df["frequency"].fillna(df["max_frequency"])

    # Operations per SM per clock cycle: TOPS to ops/s, MHz to Hz
    df["ops_per_cycle"] = df.tops * 1e12 / (df.mp_count * df.frequency * 1e6)

    # Scale measured TOPS to max frequency
    df["max_tops"] = df.tops / df.frequency * df.max_frequency

    return df


def create_styled_table(
    df: pd.DataFrame,
    value_col: str,
    row_order: List[str],
    column_order: Optional[List[str]] = None,
) -> Tuple[pd.DataFrame, "pd.io.formats.style.Styler", List[str]]:
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


def export_styled_table(
    styled, filename: str, target_width: Optional[int] = None
) -> int:
    """Export a styled table as a PNG, optionally on a fixed canvas width.

    GitHub scales every image to the container width, so a table with few
    rows or columns renders with larger text than a wide table. Padding
    each export onto one shared canvas width keeps the font size equal
    across the document. The table is centered on transparent padding.
    Returns the final pixel width.
    """
    dfi.export(styled, filename, table_conversion="matplotlib")
    with Image.open(filename) as img:
        if target_width is None or img.width >= target_width:
            return img.width
        canvas = Image.new("RGBA", (target_width, img.height), (0, 0, 0, 0))
        canvas.paste(img, ((target_width - img.width) // 2, 0))
    canvas.save(filename)
    return target_width


def generate_report(table_absolute, table_ops, table_tc, table_tc_ops) -> str:
    """Generate the markdown report content."""
    return f"""
# CUDA peak performance report

This auto-generated report presents benchmark results for the [cudapeak](https://github.com/astron-rd/cudapeak) FP32 and MMA synthetic performance benchmarks on various GPUs.

The benchmarks evaluate synthetic workloads designed to measure peak operations per second (OPs), providing insights into architectural efficiency and computational limits.

## Absolute performance
Measured in teraoperations per second (TOPs), showing raw computational throughput for various data types and MMA sizes.

![Absolute performance](performance.png)

<details>
<summary><b>Data table</b></summary>
{table_absolute.to_html()}
</details>

## Operations per SM per clock cycle
Measured in operations per SM per clock cycle, showing how performance scales across different data types.

![Operations per SM per clock cycle](ops_per_cycle.png)

<details>
<summary><b>Data table</b></summary>
{table_ops.to_html()}
</details>

## tcgen05 absolute performance
Measured in teraoperations per second (TOPs) for tcgen05 (UMMA) kernels. On Thor these kernels reach a much higher peak throughput than the warp-level kernels above.

![tcgen05 absolute performance](tcgen05_performance.png)

<details>
<summary><b>Data table</b></summary>
{table_tc.to_html()}
</details>

## tcgen05 operations per SM per clock cycle
Measured in operations per SM per clock cycle for tcgen05 (UMMA) kernels.

![tcgen05 operations per SM per clock cycle](tcgen05_ops_per_cycle.png)

<details>
<summary><b>Data table</b></summary>
{table_tc_ops.to_html()}
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

    # Warp-level tables exclude the tcgen05 kernels
    df_warp = df[~df["name"].str.startswith("tcgen05")]

    # Create styled tables
    table_performance, table_performance_styled, column_order = create_styled_table(
        df_warp, "max_tops", ROW_ORDER
    )
    table_ops, table_ops_styled, _ = create_styled_table(
        df_warp, "ops_per_cycle", ROW_ORDER, column_order
    )

    df_tc = df[df["name"].str.startswith("tcgen05")]
    table_tc, table_tc_styled, tc_column_order = create_styled_table(
        df_tc, "max_tops", TCGEN05_ROW_ORDER
    )
    table_tc_ops, table_tc_ops_styled, _ = create_styled_table(
        df_tc, "ops_per_cycle", TCGEN05_ROW_ORDER, tc_column_order
    )

    # Export styled tables as images. Wide and narrow tables share one
    # canvas width so the document renders them at the same scale.
    base_width = export_styled_table(table_performance_styled, "performance.png")
    export_styled_table(table_ops_styled, "ops_per_cycle.png", base_width)
    export_styled_table(table_tc_styled, "tcgen05_performance.png", base_width)
    export_styled_table(table_tc_ops_styled, "tcgen05_ops_per_cycle.png", base_width)

    # Generate and save report
    report_content = generate_report(
        table_performance, table_ops, table_tc, table_tc_ops
    )

    with open("README.md", "w") as f:
        f.write(report_content)

    print("Report generated successfully as README.md")


if __name__ == "__main__":
    main()

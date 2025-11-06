
# CUDA Peak Performance Report

This auto-generated report presents benchmark results for the [cudapeak](https://github.com/astron-rd/cudapeak) FP32 and MMA synthetic performance benchmarks on various GPUs.

The benchmarks evaluate synthetic workloads designed to measure peak operations per second (OPs), providing insights into architectural efficiency and computational limits.

## Absolute Performance
Measured in teraoperations per second (TOPs), showing raw computational throughput for various data types and MMA sizes.

<style type="text/css">
#T_dbc5c_row0_col0, #T_dbc5c_row10_col0 {
  background-color: #f1faee;
  color: #000000;
}
#T_dbc5c_row0_col1, #T_dbc5c_row0_col3, #T_dbc5c_row0_col4, #T_dbc5c_row0_col6, #T_dbc5c_row1_col4 {
  background-color: #f5fbf3;
  color: #000000;
}
#T_dbc5c_row0_col2, #T_dbc5c_row0_col7, #T_dbc5c_row1_col5, #T_dbc5c_row1_col7, #T_dbc5c_row10_col7 {
  background-color: #f7fcf5;
  color: #000000;
}
#T_dbc5c_row0_col5, #T_dbc5c_row10_col5 {
  background-color: #f2faf0;
  color: #000000;
}
#T_dbc5c_row1_col0 {
  background-color: #ebf7e7;
  color: #000000;
}
#T_dbc5c_row1_col1, #T_dbc5c_row1_col2, #T_dbc5c_row1_col3, #T_dbc5c_row1_col6, #T_dbc5c_row2_col4, #T_dbc5c_row3_col4 {
  background-color: #f3faf0;
  color: #000000;
}
#T_dbc5c_row2_col0, #T_dbc5c_row3_col0, #T_dbc5c_row7_col0 {
  background-color: #afdfa8;
  color: #000000;
}
#T_dbc5c_row2_col1, #T_dbc5c_row2_col3, #T_dbc5c_row2_col6, #T_dbc5c_row3_col1, #T_dbc5c_row3_col2, #T_dbc5c_row4_col4, #T_dbc5c_row5_col4 {
  background-color: #eff9eb;
  color: #000000;
}
#T_dbc5c_row2_col2 {
  background-color: #eff9ec;
  color: #000000;
}
#T_dbc5c_row2_col5, #T_dbc5c_row3_col5 {
  background-color: #e9f7e5;
  color: #000000;
}
#T_dbc5c_row2_col7, #T_dbc5c_row3_col7, #T_dbc5c_row7_col7 {
  background-color: #d3eecd;
  color: #000000;
}
#T_dbc5c_row3_col3, #T_dbc5c_row3_col6 {
  background-color: #eef8ea;
  color: #000000;
}
#T_dbc5c_row4_col0, #T_dbc5c_row5_col0, #T_dbc5c_row8_col5, #T_dbc5c_row8_col7, #T_dbc5c_row13_col1, #T_dbc5c_row13_col2, #T_dbc5c_row13_col3, #T_dbc5c_row13_col4, #T_dbc5c_row13_col6, #T_dbc5c_row14_col1, #T_dbc5c_row14_col2, #T_dbc5c_row14_col3, #T_dbc5c_row14_col4, #T_dbc5c_row14_col6 {
  background-color: #00441b;
  color: #f1f1f1;
}
#T_dbc5c_row4_col1, #T_dbc5c_row4_col2, #T_dbc5c_row5_col1, #T_dbc5c_row5_col2, #T_dbc5c_row8_col0, #T_dbc5c_row8_col1, #T_dbc5c_row8_col2, #T_dbc5c_row8_col3, #T_dbc5c_row8_col4, #T_dbc5c_row8_col6, #T_dbc5c_row9_col0, #T_dbc5c_row9_col1, #T_dbc5c_row9_col2, #T_dbc5c_row9_col3, #T_dbc5c_row9_col4, #T_dbc5c_row9_col6 {
  background-color: #f7fcf5;
  color: #000000;
  color: #f7fcf5;
}
#T_dbc5c_row4_col3, #T_dbc5c_row4_col6, #T_dbc5c_row5_col3, #T_dbc5c_row5_col6, #T_dbc5c_row6_col1, #T_dbc5c_row6_col2, #T_dbc5c_row6_col3, #T_dbc5c_row6_col6, #T_dbc5c_row7_col1, #T_dbc5c_row7_col2, #T_dbc5c_row7_col3, #T_dbc5c_row7_col4, #T_dbc5c_row7_col6, #T_dbc5c_row10_col2, #T_dbc5c_row14_col0 {
  background-color: #e5f5e1;
  color: #000000;
}
#T_dbc5c_row4_col5, #T_dbc5c_row5_col5, #T_dbc5c_row7_col5, #T_dbc5c_row9_col5 {
  background-color: #ccebc6;
  color: #000000;
}
#T_dbc5c_row4_col7, #T_dbc5c_row5_col7, #T_dbc5c_row6_col7, #T_dbc5c_row9_col7 {
  background-color: #80ca80;
  color: #000000;
}
#T_dbc5c_row6_col0 {
  background-color: #39a257;
  color: #f1f1f1;
}
#T_dbc5c_row6_col4 {
  background-color: #e5f5e0;
  color: #000000;
}
#T_dbc5c_row6_col5, #T_dbc5c_row11_col2 {
  background-color: #79c67a;
  color: #000000;
}
#T_dbc5c_row10_col1, #T_dbc5c_row10_col3, #T_dbc5c_row10_col4, #T_dbc5c_row10_col6 {
  background-color: #c8e9c1;
  color: #000000;
}
#T_dbc5c_row11_col0 {
  background-color: #d8f0d2;
  color: #000000;
}
#T_dbc5c_row11_col1, #T_dbc5c_row11_col3, #T_dbc5c_row11_col4, #T_dbc5c_row11_col6 {
  background-color: #004e1f;
  color: #f1f1f1;
}
#T_dbc5c_row11_col5 {
  background-color: #d5efcf;
  color: #000000;
}
#T_dbc5c_row11_col7 {
  background-color: #dbf1d6;
  color: #000000;
}
#T_dbc5c_row12_col0, #T_dbc5c_row12_col5 {
  background-color: #edf8ea;
  color: #000000;
}
#T_dbc5c_row12_col1, #T_dbc5c_row12_col3, #T_dbc5c_row12_col4, #T_dbc5c_row12_col6 {
  background-color: #00471c;
  color: #f1f1f1;
}
#T_dbc5c_row12_col2 {
  background-color: #75c477;
  color: #000000;
}
#T_dbc5c_row12_col7 {
  background-color: #f2faef;
  color: #000000;
}
#T_dbc5c_row13_col0 {
  background-color: #92d28f;
  color: #000000;
}
#T_dbc5c_row13_col5 {
  background-color: #84cc83;
  color: #000000;
}
#T_dbc5c_row13_col7 {
  background-color: #90d18d;
  color: #000000;
}
#T_dbc5c_row14_col5 {
  background-color: #e1f3dc;
  color: #000000;
}
#T_dbc5c_row14_col7 {
  background-color: #e7f6e3;
  color: #000000;
}
</style>
<table id="T_dbc5c">
  <thead>
    <tr>
      <th class="index_name level0" >gpu</th>
      <th id="T_dbc5c_level0_col0" class="col_heading level0 col0" >Blackwell Thor</th>
      <th id="T_dbc5c_level0_col1" class="col_heading level0 col1" >Ampere A4000</th>
      <th id="T_dbc5c_level0_col2" class="col_heading level0 col2" >Ampere A100</th>
      <th id="T_dbc5c_level0_col3" class="col_heading level0 col3" >Ada 4000</th>
      <th id="T_dbc5c_level0_col4" class="col_heading level0 col4" >Ada RTX4070</th>
      <th id="T_dbc5c_level0_col5" class="col_heading level0 col5" >Blackwell RTX5070</th>
      <th id="T_dbc5c_level0_col6" class="col_heading level0 col6" >Ada 5000</th>
      <th id="T_dbc5c_level0_col7" class="col_heading level0 col7" >Blackwell 6000</th>
    </tr>
    <tr>
      <th class="index_name level0" >name</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_dbc5c_level0_row0" class="row_heading level0 row0" >fp32</th>
      <td id="T_dbc5c_row0_col0" class="data row0 col0" >7.02</td>
      <td id="T_dbc5c_row0_col1" class="data row0 col1" >18.93</td>
      <td id="T_dbc5c_row0_col2" class="data row0 col2" >19.07</td>
      <td id="T_dbc5c_row0_col3" class="data row0 col3" >26.41</td>
      <td id="T_dbc5c_row0_col4" class="data row0 col4" >28.80</td>
      <td id="T_dbc5c_row0_col5" class="data row0 col5" >30.82</td>
      <td id="T_dbc5c_row0_col6" class="data row0 col6" >64.50</td>
      <td id="T_dbc5c_row0_col7" class="data row0 col7" >109.66</td>
    </tr>
    <tr>
      <th id="T_dbc5c_level0_row1" class="row_heading level0 row1" >mma_tf32_16_16_8</th>
      <td id="T_dbc5c_row1_col0" class="data row1 col0" >14.18</td>
      <td id="T_dbc5c_row1_col1" class="data row1 col1" >37.90</td>
      <td id="T_dbc5c_row1_col2" class="data row1 col2" >149.91</td>
      <td id="T_dbc5c_row1_col3" class="data row1 col3" >52.84</td>
      <td id="T_dbc5c_row1_col4" class="data row1 col4" >29.11</td>
      <td id="T_dbc5c_row1_col5" class="data row1 col5" >15.45</td>
      <td id="T_dbc5c_row1_col6" class="data row1 col6" >129.08</td>
      <td id="T_dbc5c_row1_col7" class="data row1 col7" >110.22</td>
    </tr>
    <tr>
      <th id="T_dbc5c_level0_row2" class="row_heading level0 row2" >mma_bf16_16_16_16</th>
      <td id="T_dbc5c_row2_col0" class="data row2 col0" >56.41</td>
      <td id="T_dbc5c_row2_col1" class="data row2 col1" >75.21</td>
      <td id="T_dbc5c_row2_col2" class="data row2 col2" >288.86</td>
      <td id="T_dbc5c_row2_col3" class="data row2 col3" >104.85</td>
      <td id="T_dbc5c_row2_col4" class="data row2 col4" >58.16</td>
      <td id="T_dbc5c_row2_col5" class="data row2 col5" >61.80</td>
      <td id="T_dbc5c_row2_col6" class="data row2 col6" >256.10</td>
      <td id="T_dbc5c_row2_col7" class="data row2 col7" >440.48</td>
    </tr>
    <tr>
      <th id="T_dbc5c_level0_row3" class="row_heading level0 row3" >mma_f16_16_16_16</th>
      <td id="T_dbc5c_row3_col0" class="data row3 col0" >56.64</td>
      <td id="T_dbc5c_row3_col1" class="data row3 col1" >76.62</td>
      <td id="T_dbc5c_row3_col2" class="data row3 col2" >308.90</td>
      <td id="T_dbc5c_row3_col3" class="data row3 col3" >106.84</td>
      <td id="T_dbc5c_row3_col4" class="data row3 col4" >58.27</td>
      <td id="T_dbc5c_row3_col5" class="data row3 col5" >61.80</td>
      <td id="T_dbc5c_row3_col6" class="data row3 col6" >260.97</td>
      <td id="T_dbc5c_row3_col7" class="data row3 col7" >440.53</td>
    </tr>
    <tr>
      <th id="T_dbc5c_level0_row4" class="row_heading level0 row4" >mma_e4m3_16_8_32</th>
      <td id="T_dbc5c_row4_col0" class="data row4 col0" >171.29</td>
      <td id="T_dbc5c_row4_col1" class="data row4 col1" >0.00</td>
      <td id="T_dbc5c_row4_col2" class="data row4 col2" >0.00</td>
      <td id="T_dbc5c_row4_col3" class="data row4 col3" >213.46</td>
      <td id="T_dbc5c_row4_col4" class="data row4 col4" >116.45</td>
      <td id="T_dbc5c_row4_col5" class="data row4 col5" >123.55</td>
      <td id="T_dbc5c_row4_col6" class="data row4 col6" >521.37</td>
      <td id="T_dbc5c_row4_col7" class="data row4 col7" >878.45</td>
    </tr>
    <tr>
      <th id="T_dbc5c_level0_row5" class="row_heading level0 row5" >mma_e5m2_16_8_32</th>
      <td id="T_dbc5c_row5_col0" class="data row5 col0" >171.28</td>
      <td id="T_dbc5c_row5_col1" class="data row5 col1" >0.00</td>
      <td id="T_dbc5c_row5_col2" class="data row5 col2" >0.00</td>
      <td id="T_dbc5c_row5_col3" class="data row5 col3" >213.46</td>
      <td id="T_dbc5c_row5_col4" class="data row5 col4" >116.45</td>
      <td id="T_dbc5c_row5_col5" class="data row5 col5" >123.54</td>
      <td id="T_dbc5c_row5_col6" class="data row5 col6" >521.37</td>
      <td id="T_dbc5c_row5_col7" class="data row5 col7" >878.44</td>
    </tr>
    <tr>
      <th id="T_dbc5c_level0_row6" class="row_heading level0 row6" >mma_s8_16_8_32</th>
      <td id="T_dbc5c_row6_col0" class="data row6 col0" >112.80</td>
      <td id="T_dbc5c_row6_col1" class="data row6 col1" >153.32</td>
      <td id="T_dbc5c_row6_col2" class="data row6 col2" >618.89</td>
      <td id="T_dbc5c_row6_col3" class="data row6 col3" >213.65</td>
      <td id="T_dbc5c_row6_col4" class="data row6 col4" >233.11</td>
      <td id="T_dbc5c_row6_col5" class="data row6 col5" >246.77</td>
      <td id="T_dbc5c_row6_col6" class="data row6 col6" >521.86</td>
      <td id="T_dbc5c_row6_col7" class="data row6 col7" >880.02</td>
    </tr>
    <tr>
      <th id="T_dbc5c_level0_row7" class="row_heading level0 row7" >mma_s8_16_16_16</th>
      <td id="T_dbc5c_row7_col0" class="data row7 col0" >56.75</td>
      <td id="T_dbc5c_row7_col1" class="data row7 col1" >152.89</td>
      <td id="T_dbc5c_row7_col2" class="data row7 col2" >618.20</td>
      <td id="T_dbc5c_row7_col3" class="data row7 col3" >213.17</td>
      <td id="T_dbc5c_row7_col4" class="data row7 col4" >232.46</td>
      <td id="T_dbc5c_row7_col5" class="data row7 col5" >123.61</td>
      <td id="T_dbc5c_row7_col6" class="data row7 col6" >520.67</td>
      <td id="T_dbc5c_row7_col7" class="data row7 col7" >440.80</td>
    </tr>
    <tr>
      <th id="T_dbc5c_level0_row8" class="row_heading level0 row8" >mma_e2m1_16_8_64</th>
      <td id="T_dbc5c_row8_col0" class="data row8 col0" >0.00</td>
      <td id="T_dbc5c_row8_col1" class="data row8 col1" >0.00</td>
      <td id="T_dbc5c_row8_col2" class="data row8 col2" >0.00</td>
      <td id="T_dbc5c_row8_col3" class="data row8 col3" >0.00</td>
      <td id="T_dbc5c_row8_col4" class="data row8 col4" >0.00</td>
      <td id="T_dbc5c_row8_col5" class="data row8 col5" >490.28</td>
      <td id="T_dbc5c_row8_col6" class="data row8 col6" >0.00</td>
      <td id="T_dbc5c_row8_col7" class="data row8 col7" >1755.17</td>
    </tr>
    <tr>
      <th id="T_dbc5c_level0_row9" class="row_heading level0 row9" >mma_e3m2_16_8_32</th>
      <td id="T_dbc5c_row9_col0" class="data row9 col0" >0.00</td>
      <td id="T_dbc5c_row9_col1" class="data row9 col1" >0.00</td>
      <td id="T_dbc5c_row9_col2" class="data row9 col2" >0.00</td>
      <td id="T_dbc5c_row9_col3" class="data row9 col3" >0.00</td>
      <td id="T_dbc5c_row9_col4" class="data row9 col4" >0.00</td>
      <td id="T_dbc5c_row9_col5" class="data row9 col5" >123.55</td>
      <td id="T_dbc5c_row9_col6" class="data row9 col6" >0.00</td>
      <td id="T_dbc5c_row9_col7" class="data row9 col7" >878.45</td>
    </tr>
    <tr>
      <th id="T_dbc5c_level0_row10" class="row_heading level0 row10" >mma_s4_8_8_32</th>
      <td id="T_dbc5c_row10_col0" class="data row10 col0" >7.07</td>
      <td id="T_dbc5c_row10_col1" class="data row10 col1" >303.52</td>
      <td id="T_dbc5c_row10_col2" class="data row10 col2" >617.21</td>
      <td id="T_dbc5c_row10_col3" class="data row10 col3" >423.17</td>
      <td id="T_dbc5c_row10_col4" class="data row10 col4" >461.47</td>
      <td id="T_dbc5c_row10_col5" class="data row10 col5" >31.77</td>
      <td id="T_dbc5c_row10_col6" class="data row10 col6" >1033.60</td>
      <td id="T_dbc5c_row10_col7" class="data row10 col7" >112.96</td>
    </tr>
    <tr>
      <th id="T_dbc5c_level0_row11" class="row_heading level0 row11" >bmma_b1_8_8_128_and</th>
      <td id="T_dbc5c_row11_col0" class="data row11 col0" >31.16</td>
      <td id="T_dbc5c_row11_col1" class="data row11 col1" >1186.33</td>
      <td id="T_dbc5c_row11_col2" class="data row11 col2" >2412.57</td>
      <td id="T_dbc5c_row11_col3" class="data row11 col3" >1654.07</td>
      <td id="T_dbc5c_row11_col4" class="data row11 col4" >1803.80</td>
      <td id="T_dbc5c_row11_col5" class="data row11 col5" >107.45</td>
      <td id="T_dbc5c_row11_col6" class="data row11 col6" >4040.06</td>
      <td id="T_dbc5c_row11_col7" class="data row11 col7" >383.10</td>
    </tr>
    <tr>
      <th id="T_dbc5c_level0_row12" class="row_heading level0 row12" >bmma_b1_8_8_128_xor</th>
      <td id="T_dbc5c_row12_col0" class="data row12 col0" >11.90</td>
      <td id="T_dbc5c_row12_col1" class="data row12 col1" >1214.06</td>
      <td id="T_dbc5c_row12_col2" class="data row12 col2" >2468.85</td>
      <td id="T_dbc5c_row12_col3" class="data row12 col3" >1692.69</td>
      <td id="T_dbc5c_row12_col4" class="data row12 col4" >1845.90</td>
      <td id="T_dbc5c_row12_col5" class="data row12 col5" >47.76</td>
      <td id="T_dbc5c_row12_col6" class="data row12 col6" >4134.36</td>
      <td id="T_dbc5c_row12_col7" class="data row12 col7" >170.38</td>
    </tr>
    <tr>
      <th id="T_dbc5c_level0_row13" class="row_heading level0 row13" >bmma_b1_16_8_256_and</th>
      <td id="T_dbc5c_row13_col0" class="data row13 col0" >71.20</td>
      <td id="T_dbc5c_row13_col1" class="data row13 col1" >1226.54</td>
      <td id="T_dbc5c_row13_col2" class="data row13 col2" >4951.13</td>
      <td id="T_dbc5c_row13_col3" class="data row13 col3" >1709.25</td>
      <td id="T_dbc5c_row13_col4" class="data row13 col4" >1864.89</td>
      <td id="T_dbc5c_row13_col5" class="data row13 col5" >232.24</td>
      <td id="T_dbc5c_row13_col6" class="data row13 col6" >4174.85</td>
      <td id="T_dbc5c_row13_col7" class="data row13 col7" >808.87</td>
    </tr>
    <tr>
      <th id="T_dbc5c_level0_row14" class="row_heading level0 row14" >bmma_b1_16_8_256_xor</th>
      <td id="T_dbc5c_row14_col0" class="data row14 col0" >20.79</td>
      <td id="T_dbc5c_row14_col1" class="data row14 col1" >1226.54</td>
      <td id="T_dbc5c_row14_col2" class="data row14 col2" >4951.11</td>
      <td id="T_dbc5c_row14_col3" class="data row14 col3" >1709.25</td>
      <td id="T_dbc5c_row14_col4" class="data row14 col4" >1864.89</td>
      <td id="T_dbc5c_row14_col5" class="data row14 col5" >82.35</td>
      <td id="T_dbc5c_row14_col6" class="data row14 col6" >4174.87</td>
      <td id="T_dbc5c_row14_col7" class="data row14 col7" >293.48</td>
    </tr>
  </tbody>
</table>


## Normalized Performance  
Scaled relative to each GPU's slowest individual benchmark result, revealing how performance scales across different data types.

<style type="text/css">
#T_d558c_row0_col0, #T_d558c_row0_col1, #T_d558c_row0_col2, #T_d558c_row0_col4, #T_d558c_row1_col2 {
  background-color: #f5fbf3;
  color: #000000;
}
#T_d558c_row0_col3, #T_d558c_row0_col5, #T_d558c_row1_col5, #T_d558c_row1_col7, #T_d558c_row10_col5 {
  background-color: #f7fcf5;
  color: #000000;
}
#T_d558c_row0_col6, #T_d558c_row10_col6 {
  background-color: #f1faee;
  color: #000000;
}
#T_d558c_row0_col7, #T_d558c_row10_col7 {
  background-color: #f2faf0;
  color: #000000;
}
#T_d558c_row1_col0, #T_d558c_row1_col1, #T_d558c_row1_col3, #T_d558c_row1_col4, #T_d558c_row2_col2, #T_d558c_row3_col2 {
  background-color: #f3faf0;
  color: #000000;
}
#T_d558c_row1_col6 {
  background-color: #ebf7e7;
  color: #000000;
}
#T_d558c_row2_col0, #T_d558c_row2_col1, #T_d558c_row2_col4, #T_d558c_row3_col3, #T_d558c_row3_col4, #T_d558c_row4_col2, #T_d558c_row5_col2 {
  background-color: #eff9eb;
  color: #000000;
}
#T_d558c_row2_col3 {
  background-color: #eff9ec;
  color: #000000;
}
#T_d558c_row2_col5, #T_d558c_row3_col5, #T_d558c_row7_col5 {
  background-color: #d3eecd;
  color: #000000;
}
#T_d558c_row2_col6, #T_d558c_row3_col6, #T_d558c_row7_col6 {
  background-color: #afdfa8;
  color: #000000;
}
#T_d558c_row2_col7, #T_d558c_row3_col7 {
  background-color: #e9f7e5;
  color: #000000;
}
#T_d558c_row3_col0, #T_d558c_row3_col1 {
  background-color: #eef8ea;
  color: #000000;
}
#T_d558c_row4_col0, #T_d558c_row4_col1, #T_d558c_row5_col0, #T_d558c_row5_col1, #T_d558c_row6_col0, #T_d558c_row6_col1, #T_d558c_row6_col3, #T_d558c_row6_col4, #T_d558c_row7_col0, #T_d558c_row7_col1, #T_d558c_row7_col2, #T_d558c_row7_col3, #T_d558c_row7_col4, #T_d558c_row10_col3, #T_d558c_row14_col6 {
  background-color: #e5f5e1;
  color: #000000;
}
#T_d558c_row4_col3, #T_d558c_row4_col4, #T_d558c_row5_col3, #T_d558c_row5_col4, #T_d558c_row8_col0, #T_d558c_row8_col1, #T_d558c_row8_col2, #T_d558c_row8_col3, #T_d558c_row8_col4, #T_d558c_row8_col6, #T_d558c_row9_col0, #T_d558c_row9_col1, #T_d558c_row9_col2, #T_d558c_row9_col3, #T_d558c_row9_col4, #T_d558c_row9_col6 {
  background-color: #f7fcf5;
  color: #000000;
  color: #f7fcf5;
}
#T_d558c_row4_col5, #T_d558c_row5_col5, #T_d558c_row6_col5, #T_d558c_row9_col5 {
  background-color: #80ca80;
  color: #000000;
}
#T_d558c_row4_col6, #T_d558c_row5_col6, #T_d558c_row8_col5, #T_d558c_row8_col7, #T_d558c_row13_col0, #T_d558c_row13_col1, #T_d558c_row13_col2, #T_d558c_row13_col3, #T_d558c_row13_col4, #T_d558c_row14_col0, #T_d558c_row14_col1, #T_d558c_row14_col2, #T_d558c_row14_col3, #T_d558c_row14_col4 {
  background-color: #00441b;
  color: #f1f1f1;
}
#T_d558c_row4_col7, #T_d558c_row5_col7, #T_d558c_row7_col7, #T_d558c_row9_col7 {
  background-color: #ccebc6;
  color: #000000;
}
#T_d558c_row6_col2 {
  background-color: #e5f5e0;
  color: #000000;
}
#T_d558c_row6_col6 {
  background-color: #39a257;
  color: #f1f1f1;
}
#T_d558c_row6_col7, #T_d558c_row11_col3 {
  background-color: #79c67a;
  color: #000000;
}
#T_d558c_row10_col0, #T_d558c_row10_col1, #T_d558c_row10_col2, #T_d558c_row10_col4 {
  background-color: #c8e9c1;
  color: #000000;
}
#T_d558c_row11_col0, #T_d558c_row11_col1, #T_d558c_row11_col2, #T_d558c_row11_col4 {
  background-color: #004e1f;
  color: #f1f1f1;
}
#T_d558c_row11_col5 {
  background-color: #dbf1d6;
  color: #000000;
}
#T_d558c_row11_col6 {
  background-color: #d8f0d2;
  color: #000000;
}
#T_d558c_row11_col7 {
  background-color: #d5efcf;
  color: #000000;
}
#T_d558c_row12_col0, #T_d558c_row12_col1, #T_d558c_row12_col2, #T_d558c_row12_col4 {
  background-color: #00471c;
  color: #f1f1f1;
}
#T_d558c_row12_col3 {
  background-color: #75c477;
  color: #000000;
}
#T_d558c_row12_col5 {
  background-color: #f2faef;
  color: #000000;
}
#T_d558c_row12_col6, #T_d558c_row12_col7 {
  background-color: #edf8ea;
  color: #000000;
}
#T_d558c_row13_col5 {
  background-color: #90d18d;
  color: #000000;
}
#T_d558c_row13_col6 {
  background-color: #92d28f;
  color: #000000;
}
#T_d558c_row13_col7 {
  background-color: #84cc83;
  color: #000000;
}
#T_d558c_row14_col5 {
  background-color: #e7f6e3;
  color: #000000;
}
#T_d558c_row14_col7 {
  background-color: #e1f3dc;
  color: #000000;
}
</style>
<table id="T_d558c">
  <thead>
    <tr>
      <th class="index_name level0" >gpu</th>
      <th id="T_d558c_level0_col0" class="col_heading level0 col0" >Ada 4000</th>
      <th id="T_d558c_level0_col1" class="col_heading level0 col1" >Ada 5000</th>
      <th id="T_d558c_level0_col2" class="col_heading level0 col2" >Ada RTX4070</th>
      <th id="T_d558c_level0_col3" class="col_heading level0 col3" >Ampere A100</th>
      <th id="T_d558c_level0_col4" class="col_heading level0 col4" >Ampere A4000</th>
      <th id="T_d558c_level0_col5" class="col_heading level0 col5" >Blackwell 6000</th>
      <th id="T_d558c_level0_col6" class="col_heading level0 col6" >Blackwell Thor</th>
      <th id="T_d558c_level0_col7" class="col_heading level0 col7" >Blackwell RTX5070</th>
    </tr>
    <tr>
      <th class="index_name level0" >name</th>
      <th class="blank col0" >&nbsp;</th>
      <th class="blank col1" >&nbsp;</th>
      <th class="blank col2" >&nbsp;</th>
      <th class="blank col3" >&nbsp;</th>
      <th class="blank col4" >&nbsp;</th>
      <th class="blank col5" >&nbsp;</th>
      <th class="blank col6" >&nbsp;</th>
      <th class="blank col7" >&nbsp;</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T_d558c_level0_row0" class="row_heading level0 row0" >fp32</th>
      <td id="T_d558c_row0_col0" class="data row0 col0" >1.00</td>
      <td id="T_d558c_row0_col1" class="data row0 col1" >1.00</td>
      <td id="T_d558c_row0_col2" class="data row0 col2" >1.00</td>
      <td id="T_d558c_row0_col3" class="data row0 col3" >1.00</td>
      <td id="T_d558c_row0_col4" class="data row0 col4" >1.00</td>
      <td id="T_d558c_row0_col5" class="data row0 col5" >1.00</td>
      <td id="T_d558c_row0_col6" class="data row0 col6" >1.00</td>
      <td id="T_d558c_row0_col7" class="data row0 col7" >1.99</td>
    </tr>
    <tr>
      <th id="T_d558c_level0_row1" class="row_heading level0 row1" >mma_tf32_16_16_8</th>
      <td id="T_d558c_row1_col0" class="data row1 col0" >2.00</td>
      <td id="T_d558c_row1_col1" class="data row1 col1" >2.00</td>
      <td id="T_d558c_row1_col2" class="data row1 col2" >1.01</td>
      <td id="T_d558c_row1_col3" class="data row1 col3" >7.86</td>
      <td id="T_d558c_row1_col4" class="data row1 col4" >2.00</td>
      <td id="T_d558c_row1_col5" class="data row1 col5" >1.01</td>
      <td id="T_d558c_row1_col6" class="data row1 col6" >2.02</td>
      <td id="T_d558c_row1_col7" class="data row1 col7" >1.00</td>
    </tr>
    <tr>
      <th id="T_d558c_level0_row2" class="row_heading level0 row2" >mma_bf16_16_16_16</th>
      <td id="T_d558c_row2_col0" class="data row2 col0" >3.97</td>
      <td id="T_d558c_row2_col1" class="data row2 col1" >3.97</td>
      <td id="T_d558c_row2_col2" class="data row2 col2" >2.02</td>
      <td id="T_d558c_row2_col3" class="data row2 col3" >15.15</td>
      <td id="T_d558c_row2_col4" class="data row2 col4" >3.97</td>
      <td id="T_d558c_row2_col5" class="data row2 col5" >4.02</td>
      <td id="T_d558c_row2_col6" class="data row2 col6" >8.04</td>
      <td id="T_d558c_row2_col7" class="data row2 col7" >4.00</td>
    </tr>
    <tr>
      <th id="T_d558c_level0_row3" class="row_heading level0 row3" >mma_f16_16_16_16</th>
      <td id="T_d558c_row3_col0" class="data row3 col0" >4.05</td>
      <td id="T_d558c_row3_col1" class="data row3 col1" >4.05</td>
      <td id="T_d558c_row3_col2" class="data row3 col2" >2.02</td>
      <td id="T_d558c_row3_col3" class="data row3 col3" >16.20</td>
      <td id="T_d558c_row3_col4" class="data row3 col4" >4.05</td>
      <td id="T_d558c_row3_col5" class="data row3 col5" >4.02</td>
      <td id="T_d558c_row3_col6" class="data row3 col6" >8.07</td>
      <td id="T_d558c_row3_col7" class="data row3 col7" >4.00</td>
    </tr>
    <tr>
      <th id="T_d558c_level0_row4" class="row_heading level0 row4" >mma_e4m3_16_8_32</th>
      <td id="T_d558c_row4_col0" class="data row4 col0" >8.08</td>
      <td id="T_d558c_row4_col1" class="data row4 col1" >8.08</td>
      <td id="T_d558c_row4_col2" class="data row4 col2" >4.04</td>
      <td id="T_d558c_row4_col3" class="data row4 col3" >0.00</td>
      <td id="T_d558c_row4_col4" class="data row4 col4" >0.00</td>
      <td id="T_d558c_row4_col5" class="data row4 col5" >8.01</td>
      <td id="T_d558c_row4_col6" class="data row4 col6" >24.40</td>
      <td id="T_d558c_row4_col7" class="data row4 col7" >7.99</td>
    </tr>
    <tr>
      <th id="T_d558c_level0_row5" class="row_heading level0 row5" >mma_e5m2_16_8_32</th>
      <td id="T_d558c_row5_col0" class="data row5 col0" >8.08</td>
      <td id="T_d558c_row5_col1" class="data row5 col1" >8.08</td>
      <td id="T_d558c_row5_col2" class="data row5 col2" >4.04</td>
      <td id="T_d558c_row5_col3" class="data row5 col3" >0.00</td>
      <td id="T_d558c_row5_col4" class="data row5 col4" >0.00</td>
      <td id="T_d558c_row5_col5" class="data row5 col5" >8.01</td>
      <td id="T_d558c_row5_col6" class="data row5 col6" >24.40</td>
      <td id="T_d558c_row5_col7" class="data row5 col7" >7.99</td>
    </tr>
    <tr>
      <th id="T_d558c_level0_row6" class="row_heading level0 row6" >mma_s8_16_8_32</th>
      <td id="T_d558c_row6_col0" class="data row6 col0" >8.09</td>
      <td id="T_d558c_row6_col1" class="data row6 col1" >8.09</td>
      <td id="T_d558c_row6_col2" class="data row6 col2" >8.09</td>
      <td id="T_d558c_row6_col3" class="data row6 col3" >32.46</td>
      <td id="T_d558c_row6_col4" class="data row6 col4" >8.10</td>
      <td id="T_d558c_row6_col5" class="data row6 col5" >8.03</td>
      <td id="T_d558c_row6_col6" class="data row6 col6" >16.07</td>
      <td id="T_d558c_row6_col7" class="data row6 col7" >15.97</td>
    </tr>
    <tr>
      <th id="T_d558c_level0_row7" class="row_heading level0 row7" >mma_s8_16_16_16</th>
      <td id="T_d558c_row7_col0" class="data row7 col0" >8.07</td>
      <td id="T_d558c_row7_col1" class="data row7 col1" >8.07</td>
      <td id="T_d558c_row7_col2" class="data row7 col2" >8.07</td>
      <td id="T_d558c_row7_col3" class="data row7 col3" >32.42</td>
      <td id="T_d558c_row7_col4" class="data row7 col4" >8.08</td>
      <td id="T_d558c_row7_col5" class="data row7 col5" >4.02</td>
      <td id="T_d558c_row7_col6" class="data row7 col6" >8.08</td>
      <td id="T_d558c_row7_col7" class="data row7 col7" >8.00</td>
    </tr>
    <tr>
      <th id="T_d558c_level0_row8" class="row_heading level0 row8" >mma_e2m1_16_8_64</th>
      <td id="T_d558c_row8_col0" class="data row8 col0" >0.00</td>
      <td id="T_d558c_row8_col1" class="data row8 col1" >0.00</td>
      <td id="T_d558c_row8_col2" class="data row8 col2" >0.00</td>
      <td id="T_d558c_row8_col3" class="data row8 col3" >0.00</td>
      <td id="T_d558c_row8_col4" class="data row8 col4" >0.00</td>
      <td id="T_d558c_row8_col5" class="data row8 col5" >16.01</td>
      <td id="T_d558c_row8_col6" class="data row8 col6" >0.00</td>
      <td id="T_d558c_row8_col7" class="data row8 col7" >31.72</td>
    </tr>
    <tr>
      <th id="T_d558c_level0_row9" class="row_heading level0 row9" >mma_e3m2_16_8_32</th>
      <td id="T_d558c_row9_col0" class="data row9 col0" >0.00</td>
      <td id="T_d558c_row9_col1" class="data row9 col1" >0.00</td>
      <td id="T_d558c_row9_col2" class="data row9 col2" >0.00</td>
      <td id="T_d558c_row9_col3" class="data row9 col3" >0.00</td>
      <td id="T_d558c_row9_col4" class="data row9 col4" >0.00</td>
      <td id="T_d558c_row9_col5" class="data row9 col5" >8.01</td>
      <td id="T_d558c_row9_col6" class="data row9 col6" >0.00</td>
      <td id="T_d558c_row9_col7" class="data row9 col7" >7.99</td>
    </tr>
    <tr>
      <th id="T_d558c_level0_row10" class="row_heading level0 row10" >mma_s4_8_8_32</th>
      <td id="T_d558c_row10_col0" class="data row10 col0" >16.02</td>
      <td id="T_d558c_row10_col1" class="data row10 col1" >16.03</td>
      <td id="T_d558c_row10_col2" class="data row10 col2" >16.02</td>
      <td id="T_d558c_row10_col3" class="data row10 col3" >32.37</td>
      <td id="T_d558c_row10_col4" class="data row10 col4" >16.03</td>
      <td id="T_d558c_row10_col5" class="data row10 col5" >1.03</td>
      <td id="T_d558c_row10_col6" class="data row10 col6" >1.01</td>
      <td id="T_d558c_row10_col7" class="data row10 col7" >2.06</td>
    </tr>
    <tr>
      <th id="T_d558c_level0_row11" class="row_heading level0 row11" >bmma_b1_8_8_128_and</th>
      <td id="T_d558c_row11_col0" class="data row11 col0" >62.64</td>
      <td id="T_d558c_row11_col1" class="data row11 col1" >62.64</td>
      <td id="T_d558c_row11_col2" class="data row11 col2" >62.64</td>
      <td id="T_d558c_row11_col3" class="data row11 col3" >126.53</td>
      <td id="T_d558c_row11_col4" class="data row11 col4" >62.67</td>
      <td id="T_d558c_row11_col5" class="data row11 col5" >3.49</td>
      <td id="T_d558c_row11_col6" class="data row11 col6" >4.44</td>
      <td id="T_d558c_row11_col7" class="data row11 col7" >6.95</td>
    </tr>
    <tr>
      <th id="T_d558c_level0_row12" class="row_heading level0 row12" >bmma_b1_8_8_128_xor</th>
      <td id="T_d558c_row12_col0" class="data row12 col0" >64.10</td>
      <td id="T_d558c_row12_col1" class="data row12 col1" >64.10</td>
      <td id="T_d558c_row12_col2" class="data row12 col2" >64.10</td>
      <td id="T_d558c_row12_col3" class="data row12 col3" >129.48</td>
      <td id="T_d558c_row12_col4" class="data row12 col4" >64.13</td>
      <td id="T_d558c_row12_col5" class="data row12 col5" >1.55</td>
      <td id="T_d558c_row12_col6" class="data row12 col6" >1.69</td>
      <td id="T_d558c_row12_col7" class="data row12 col7" >3.09</td>
    </tr>
    <tr>
      <th id="T_d558c_level0_row13" class="row_heading level0 row13" >bmma_b1_16_8_256_and</th>
      <td id="T_d558c_row13_col0" class="data row13 col0" >64.73</td>
      <td id="T_d558c_row13_col1" class="data row13 col1" >64.73</td>
      <td id="T_d558c_row13_col2" class="data row13 col2" >64.76</td>
      <td id="T_d558c_row13_col3" class="data row13 col3" >259.67</td>
      <td id="T_d558c_row13_col4" class="data row13 col4" >64.79</td>
      <td id="T_d558c_row13_col5" class="data row13 col5" >7.38</td>
      <td id="T_d558c_row13_col6" class="data row13 col6" >10.14</td>
      <td id="T_d558c_row13_col7" class="data row13 col7" >15.03</td>
    </tr>
    <tr>
      <th id="T_d558c_level0_row14" class="row_heading level0 row14" >bmma_b1_16_8_256_xor</th>
      <td id="T_d558c_row14_col0" class="data row14 col0" >64.73</td>
      <td id="T_d558c_row14_col1" class="data row14 col1" >64.73</td>
      <td id="T_d558c_row14_col2" class="data row14 col2" >64.76</td>
      <td id="T_d558c_row14_col3" class="data row14 col3" >259.67</td>
      <td id="T_d558c_row14_col4" class="data row14 col4" >64.79</td>
      <td id="T_d558c_row14_col5" class="data row14 col5" >2.68</td>
      <td id="T_d558c_row14_col6" class="data row14 col6" >2.96</td>
      <td id="T_d558c_row14_col7" class="data row14 col7" >5.33</td>
    </tr>
  </tbody>
</table>


*Report generated on 2025-11-06 15:10 UTC*

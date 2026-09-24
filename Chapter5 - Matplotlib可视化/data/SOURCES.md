# 本章唯一数据：Bike Sharing 日表

- 作者：Hadi Fanaee-T；数据集发布于 2013 年。
- 官方页面：https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset
- DOI：https://doi.org/10.24432/C5W894
- 下载地址：https://archive.ics.uci.edu/static/public/275/bike%2Bsharing%2Bdataset.zip
- 获取日期：2026-09-24。
- 许可：UCI 数据页标明 CC BY 4.0，https://creativecommons.org/licenses/by/4.0/ 。保留署名、来源和改动说明。
- 相关论文：Fanaee-T, H. and Gama, J. (2013), *Event labeling combining ensemble detectors and background knowledge*, DOI: 10.1007/s13748-013-0040-3。

`day.csv` 是官方 ZIP 中的日表，原样保存；`UCI_Readme.txt` 是原压缩包说明。未采用小时表，也未合并其他数据。中文课件、图形与练习为本课程编写。

## 范围与观察单位

Capital Bikeshare，2011-01-01 至 2012-12-31，731 行、16 列。每行是一整天的汇总；租车量是次数，不是去重人数。当前本地日表无缺失、无重复日期、日期连续，并且每行 `casual + registered == cnt`。这些是本文件的实际检查结果，不使用 UCI 网页上同时涉及小时表的总行数。

## 逐步使用的列

| 字段 | 课堂含义 | 首次使用 |
|---|---|---|
| `cnt` | 当天总租车次数 | 单变量直方图 |
| `workingday` | 1：非周末且非节假日；0：其他日子 | 分组均值柱状图 |
| `dteday` | 日期 | 每日折线与月内日均值 |
| `casual` | 临时用户租车次数 | 构成、多曲线、分组柱状图 |
| `registered` | 注册用户租车次数 | 构成与面积填充 |
| `temp` | 标准化温度，无量纲 | 散点图 |
| `yr` | 0：2011；1：2012 | 按年份分组散点 |
| `hum` | 标准化湿度，乘 100 为百分比 | 课后练习 |
| `weathersit` | 天气类别；本日表出现 1、2、3 | 课后练习 |

## 口径选择与已知来源差异

UCI 当前网页与 ZIP 内原 Readme 对温度换算公式、季节编码的说明不一致。本章直接使用 `temp` 标准化值，并明确标注无量纲；不还原摄氏温度，不解码 `season`。这不影响本章按日计数、日期汇总与类别比较。

所有图形来自一个 `bike` 表。排序不改变行数；`head(7)` 仅用于同一表的局部教学；`resample("MS").mean()` 生成 24 个月内日均值，不是月度总量。两组工作日比较用均值并给出各组天数，未删除观测或填补缺失。

这是历史样本的描述性探索，年份、天气与租车量的图形关联不等于因果效应。

"""生成同源的课堂文件；从课程根目录用 .venv 中的 Python 运行。"""
from pathlib import Path
import argparse

import numpy as np
import pandas as pd

CHAPTER = Path(__file__).resolve().parents[1]
FORMATS = {"CSV": "csv", "Excel": "xlsx", "Parquet": "parquet"}


def make_quotes(rows=20_000, seed=7):
    """每行是一只虚构证券的一条分钟观测，不代表真实市场。"""
    rng = np.random.default_rng(seed)
    price = rng.integers(1000, 10000, rows) / 100
    frame = pd.DataFrame({
        "date": pd.date_range("2025-01-01", periods=rows, freq="min"),
        "symbol": np.resize(["000001", "000002", "000003"], rows),
        "market": np.resize(["模拟市场甲", "模拟市场甲", "模拟市场乙"], rows),
        "price": price,
        "volume": rng.integers(100, 10000, rows),
        "bid": (price - 0.01).round(2),
        "ask": (price + 0.01).round(2),
        "score": rng.normal(size=rows).round(6),
    })
    frame.loc[frame.index % 17 == 0, "score"] = np.nan
    return frame


def write_formats(frame, directory):
    directory.mkdir(parents=True, exist_ok=True)
    frame.to_csv(directory / "quotes.csv", index=False, encoding="utf-8")
    frame.to_excel(directory / "quotes.xlsx", index=False,
                   sheet_name="quotes", engine="openpyxl")
    frame.to_parquet(directory / "quotes.parquet", index=False,
                     engine="pyarrow", compression="snappy", row_group_size=5000)


def prepare(rows=20_000):
    frame = make_quotes(rows)
    root = CHAPTER / "data"
    write_formats(frame, root)
    # 分区是文件夹层级；行组是每个文件内部的结构。两者不同。
    # 使用固定文件名，重复运行覆盖这两个教学文件，不追加重复记录。
    for market, group in frame.groupby("market", sort=True):
        folder = root / "quotes_by_market" / f"market={market}"
        folder.mkdir(parents=True, exist_ok=True)
        group.drop(columns="market").to_parquet(
            folder / "part-0.parquet", index=False, engine="pyarrow",
            compression="snappy", row_group_size=5000)
    return frame, root


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--rows", type=int, default=20_000)
    args = parser.parse_args()
    if not 6 <= args.rows <= 1_000_000:
        parser.error("--rows 必须在 6 到 1000000 之间（兼顾 Excel 行数限制）")
    data, folder = prepare(args.rows)
    print(f"已生成 {len(data):,} 行 × {data.shape[1]} 列的三种文件及分区示例：{folder}")

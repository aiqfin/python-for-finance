"""教师运行一次：从第11章现有Parquet抽取三股教学样本，不改写源数据。"""
from pathlib import Path
import json

import numpy as np
import pandas as pd

LAB = Path(__file__).resolve().parents[1]
SOURCE = LAB.parent / "Chapter11 - 股票日频收益率分析" / "data" / "stock_daily.parquet"
DATA = LAB / "data"
DATA.mkdir(exist_ok=True)
CODES = ["000001", "600000", "600519"]
COLUMNS = ["Stkcd", "Trddt", "Clsprc", "Dretwd", "Dnshrtrd", "Dnvaltrd"]

raw = pd.read_parquet(
    SOURCE,
    columns=COLUMNS + ["Markettype", "Filling"],
    filters=[("Stkcd", "in", CODES),
             ("Trddt", ">=", pd.Timestamp("2025-01-01")),
             ("Trddt", "<", pd.Timestamp("2026-01-01"))],
)
# 与第11章主样本一致：A股、非填充、有成交、正价格、收益率可计算。
keep = (
    raw["Markettype"].isin([1, 4, 16, 32, 64])
    & raw["Filling"].eq(0)
    & raw["Dnshrtrd"].gt(0)
    & raw["Clsprc"].gt(0)
    & np.isfinite(raw["Dretwd"])
    & raw["Dretwd"].gt(-1)
)
sample = raw.loc[keep, COLUMNS].sort_values(["Stkcd", "Trddt"]).reset_index(drop=True)
assert not sample.duplicated(["Stkcd", "Trddt"]).any()
assert set(sample["Stkcd"]) == set(CODES)
assert sample[COLUMNS].notna().all().all()
wide = sample.pivot(index="Trddt", columns="Stkcd", values="Dretwd")
# 本期三股的日期必须完整一致，才能直接比较累计收益曲线。
# 变更年份或股票后，应重新设计样本，而不能删掉中间日期后冒充完整持有收益。
assert wide.notna().all().all(), "三股有效日期不一致，请检查样本覆盖后再设计累计收益比较。"
sample.to_csv(DATA / "stocks_2025.csv", index=False, encoding="utf-8-sig", date_format="%Y-%m-%d")
summary = {
    "source": str(SOURCE.relative_to(LAB.parent)),
    "raw_selected_rows": len(raw), "sample_rows": len(sample),
    "excluded_rows": int((~keep).sum()),
    "start": str(sample.Trddt.min().date()), "end": str(sample.Trddt.max().date()),
    "counts": {str(k): int(v) for k, v in sample.groupby("Stkcd").size().items()},
    "common_dates": len(wide), "columns": COLUMNS,
}
(DATA / "sample_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False, indent=2))

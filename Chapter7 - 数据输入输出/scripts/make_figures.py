"""从实际教学文件绘制预览图与结构图；不是第三方软件截图。"""
from pathlib import Path
import argparse

import pandas as pd
import pyarrow.parquet as pq
from PIL import Image, ImageDraw, ImageFont

CHAPTER = Path(__file__).resolve().parents[1]
DATA = CHAPTER / "data"
FIGURES = CHAPTER / "latex" / "figures"
BLUE, INK, MUTED = "#003D73", "#213547", "#52677C"
PALE, LINE, GOLD = "#EFF5FA", "#CAD7E2", "#B48530"


def render_all(font_path):
    FIGURES.mkdir(parents=True, exist_ok=True)
    fonts = {size: ImageFont.truetype(str(font_path), size) for size in [20, 23, 25, 28, 32, 44]}

    def canvas(title, subtitle):
        im = Image.new("RGB", (1800, 1120), "white")
        d = ImageDraw.Draw(im)
        d.rectangle((0, 0, 1800, 12), fill=BLUE)
        d.text((55, 40), title, font=fonts[44], fill=BLUE)
        d.text((55, 105), subtitle, font=fonts[25], fill=MUTED)
        return im, d

    def text(d, xy, value, size=25, color=INK):
        d.text(xy, str(value), font=fonts[size], fill=color)

    def panel(d, box, title):
        d.rounded_rectangle(box, radius=12, fill=PALE, outline=LINE, width=2)
        text(d, (box[0]+22, box[1]+16), title, 28, BLUE)

    def table(d, frame, x, y, widths):
        row_h = 46
        for row_num, row in enumerate([list(frame.columns)] + frame.astype(str).values.tolist()):
            left = x
            for value, width in zip(row, widths):
                top = y + row_num*row_h
                d.rectangle((left, top, left+width, top+row_h),
                            fill=BLUE if row_num == 0 else ("white" if row_num % 2 else PALE),
                            outline=LINE)
                text(d, (left+12, top+8), value, 23, "white" if row_num == 0 else INK)
                left += width

    csv = pd.read_csv(DATA / "quotes.csv", dtype={"symbol": str}, parse_dates=["date"])
    excel = pd.read_excel(DATA / "quotes.xlsx", dtype={"symbol": str}, engine="openpyxl")
    parquet = pd.read_parquet(DATA / "quotes.parquet", engine="pyarrow")
    meta = pq.ParquetFile(DATA / "quotes.parquet")
    im, d = canvas("同一份行情，三种文件预览", "基于实际生成文件绘制的教学界面 · 每个文件含相同记录 · 只展示前 3 行")
    panel(d, (55, 170, 1745, 380), "CSV  |  data/quotes.csv  |  文本视图")
    lines = (DATA / "quotes.csv").read_text(encoding="utf-8").splitlines()[:4]
    for i,line in enumerate(lines): text(d, (80, 230+i*32), line, 23)
    cols = list(csv.columns)
    for frame, y, name in [(excel, 410, "Excel  |  data/quotes.xlsx  |  工作表 quotes"),
                           (parquet, 710, "Parquet  |  data/quotes.parquet  |  解码后的表格视图")]:
        panel(d, (55, y, 1745, y+270), name)
        shown = frame[cols].head(3).copy()
        shown["date"] = pd.to_datetime(shown["date"]).dt.strftime("%Y-%m-%d %H:%M:%S")
        shown = shown.astype(object).where(shown.notna(), "缺失")
        table(d, shown, 80, y+65, [360, 170, 260, 140, 140, 140, 140, 280])
    text(d, (60, 1010), "三种预览均展示相同的前 3 行、全部 8 列，列的顺序一致。", 25)
    text(d, (60, 1055), "Parquet 的表格来自读取器；原始文件是二进制，不能直接当文本浏览。", 25, BLUE)
    im.save(FIGURES / "formats_preview.png")

    im, d = canvas("一个 Parquet 文件的内部", "实际元数据来自 data/quotes.parquet · 结构示意，不按字节比例绘制")
    m = meta.metadata
    panel(d, (55, 170, 1745, 280), f"{m.num_rows:,} 行  ×  {m.num_columns} 列    |    {m.num_row_groups} 个行组    |    {m.row_group(0).column(0).compression}")
    text(d, (80, 227), "文件中的行组和列块不是操作系统文件夹；读取器通过元数据定位它们。", 25)
    # Default classroom data has four row groups; larger experiments display a bounded preview.
    shown_groups = min(m.num_row_groups, 4)
    for g in range(shown_groups):
        top = 310 + g*130
        text(d, (70, top), f"行组 {g}：{m.row_group(g).num_rows:,} 行", 25, BLUE)
        for j in range(m.num_columns):
            col = m.row_group(g).column(j)
            left = 80+j*205
            d.rectangle((left, top+43, left+190, top+98), fill=PALE, outline=LINE, width=2)
            text(d, (left+12, top+55), col.path_in_schema, 23)
    panel(d, (55, 855, 1745, 1030), "文件尾部：元数据（Footer）")
    text(d, (80, 917), "模式 / 类型  ·  行组行数  ·  列块位置  ·  各列统计信息", 28)
    text(d, (80, 969), "读取 price、volume：在各行组中定位这两列；每个列块内部再分成页。", 25)
    text(d, (60, 1060), f"显示前 {shown_groups} 个行组；共 {m.num_row_groups} 个。页的编码和压缩细节未按比例展开。", 23, MUTED)
    im.save(FIGURES / "parquet_layout.png")

    im, d = canvas("多个 Parquet 文件如何放进目录？", "实际目录：data/quotes_by_market/ · 按 market 分区 · 目录名保存分区值")
    panel(d, (55, 175, 910, 825), "目录视图  |  真实文件名")
    text(d, (90, 250), "data/", 32, BLUE)
    text(d, (120, 310), "quotes.parquet     ← 单个完整表文件", 28)
    text(d, (120, 385), "quotes_by_market/", 32, BLUE)
    parts = sorted((DATA / "quotes_by_market").glob("*/*.parquet"))
    for i,path in enumerate(parts):
        top = 455+i*165
        text(d, (165, top), path.parent.name + "/", 28, BLUE)
        text(d, (210, top+53), path.name, 28)
        pm = pq.ParquetFile(path).metadata
        text(d, (210, top+99), f"{pm.num_rows:,} 行 · {path.stat().st_size/1024:.1f} KiB", 23, MUTED)
    panel(d, (950, 175, 1745, 825), "选中文件  |  内容检查")
    selected = parts[0]
    pf = pq.ParquetFile(selected)
    text(d, (980, 250), selected.parent.name, 28, BLUE)
    text(d, (980, 307), f"{selected.name}  /  {pf.metadata.num_columns} 列", 28)
    text(d, (980, 380), "文件内的列：", 25)
    for i,col in enumerate(pf.schema_arrow.names):
        text(d, (1010, 425+i*43), f"{col}  :  {pf.schema_arrow.field(col).type}", 25)
    text(d, (980, 755), "market 从目录名恢复，不在文件内重复存。", 23, BLUE)
    panel(d, (55, 860, 1745, 1030), "读取逻辑")
    text(d, (80, 925), "读数据集根目录 → 合并两个分区；筛选市场甲 → 可以跳过市场乙文件。", 28)
    text(d, (80, 978), "普通三格式计时仍使用 data/ 下的单文件；这个目录仅用于分区教学。", 25)
    text(d, (60, 1060), "这是 Hive 风格目录分区示例；单个 .parquet 文件不要求这样的目录层级。", 23, MUTED)
    im.save(FIGURES / "parquet_directory.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--font", type=Path, default=Path("C:/Windows/Fonts/msyh.ttc"),
                        help="中文字体路径；非 Windows 系统请显式指定")
    render_all(parser.parse_args().font)
    print(FIGURES)

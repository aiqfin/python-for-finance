"""运行配套 Notebook 的代码重建共享单车插图，不改写 Notebook。"""
from pathlib import Path
import json
import os
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CHAPTER = Path(__file__).resolve().parents[1]
FIGURES = CHAPTER / "latex/figures/bike"
FIGURES.mkdir(parents=True, exist_ok=True)
notebook = json.loads((CHAPTER / "notebooks/05_Visualization.ipynb").read_text(encoding="utf-8"))
tex = (CHAPTER / "latex/chapter5.tex").read_text(encoding="utf-8")
os.chdir(CHAPTER)
scope = {"__name__": "__main__"}
generated = []

for cell in notebook["cells"]:
    if cell["cell_type"] != "code":
        continue
    source = "".join(cell["source"])
    lesson = cell["metadata"].get("lesson", {})
    if "slide_title" in lesson:
        title = lesson["slide_title"]
        tex_title = title.replace("_", r"\_")
        pattern = r"\\begin\{frame\}\[fragile\]\{" + re.escape(tex_title) + r"\}(.*?)\\end\{frame\}"
        frame = re.search(pattern, tex, re.S).group(1)
        listing = re.search(r"\\begin\{lstlisting\}(.*?)\\end\{lstlisting\}", frame, re.S).group(1)
        if source.strip() != listing.strip():
            raise ValueError(f"Notebook 与课件代码不一致：{title}")
    exec(compile(source.replace("plt.show()", ""), f"notebook:{cell['id']}", "exec"), scope)
    if "figure" in lesson:
        path = FIGURES / f"{lesson['figure']}.png"
        scope["fig"].savefig(path, dpi=180, bbox_inches="tight")
        plt.close(scope["fig"])
        generated.append(path.name)

print(f"Generated {len(generated)} figures from data/day.csv:")
print("\n".join(generated))

"""Export saved notebook figures for the slides; run the notebook first."""
from pathlib import Path
import base64
import json

chapter = Path(__file__).resolve().parents[1]
notebook = json.loads((chapter / 'notebooks/08_Math_Tools.ipynb').read_text(encoding='utf-8'))
destination = chapter / 'latex/figures'
destination.mkdir(exist_ok=True)
for cell in notebook['cells']:
    name = cell.get('metadata', {}).get('slide_figure')
    if name:
        pictures = [output['data']['image/png'] for output in cell.get('outputs', [])
                    if 'image/png' in output.get('data', {})]
        if not pictures:
            raise ValueError(f'Run the figure cell before exporting: {name}')
        destination.joinpath(name + '.png').write_bytes(base64.b64decode(pictures[-1]))
        print(name + '.png')

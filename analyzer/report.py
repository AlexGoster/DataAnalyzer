"""HTML report generator."""

from pathlib import Path
from datetime import datetime
import pandas as pd


class ReportGenerator:
    def __init__(self, output_path: str = "report.html"):
        self.output_path = Path(output_path)

    def generate(self, df: pd.DataFrame, title: str = "Data Analysis Report") -> Path:
        stats = df.describe(include="all").to_html(classes="stats-table")
        nulls = df.isnull().sum().to_frame("nulls").to_html(classes="nulls-table")
        dtypes = df.dtypes.to_frame("dtype").to_html(classes="dtypes-table")

        html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{title}</title>
<style>
body {{ font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }}
h1 {{ color: #333; border-bottom: 2px solid #e8734a; padding-bottom: 10px; }}
h2 {{ color: #555; margin-top: 30px; }}
table {{ border-collapse: collapse; width: 100%; margin: 10px 0 30px 0; }}
th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
th {{ background: #242424; color: white; }}
tr:nth-child(even) {{ background: #f2f2f2; }}
.stats-table th {{ background: #e8734a; }}
</style></head>
<body>
<h1>{title}</h1>
<p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
<p>Rows: {len(df)}, Columns: {len(df.columns)}</p>

<h2>Statistics</h2>{stats}
<h2>Missing Values</h2>{nulls}
<h2>Column Types</h2>{dtypes}
</body></html>"""

        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.output_path.write_text(html, encoding="utf-8")
        return self.output_path

from pathlib import Path
import subprocess
import sys

import pandas as pd
import pytest

from analyzer.cleaner import fill_nulls
from analyzer.report import ReportGenerator


def test_cleaning_fills_values_without_mutating_input():
    original = pd.DataFrame({"number": [1.0, None, 3.0], "text": ["a", None, "b"]})
    cleaned = fill_nulls(original)
    assert cleaned.loc[1, "number"] == 2
    assert cleaned.loc[1, "text"] == "Unknown"
    assert original.isna().sum().sum() == 2
    with pytest.raises(ValueError):
        fill_nulls(original, strategy="invalid")


def test_report_escapes_title(tmp_path):
    path = ReportGenerator(str(tmp_path / "report.html")).generate(
        pd.DataFrame({"value": [1, 2]}), title="<script>alert(1)</script>"
    )
    assert "<script>" not in path.read_text()
    assert "&lt;script&gt;" in path.read_text()


def test_installed_console_entrypoint(tmp_path):
    entrypoint = Path(sys.executable).with_name("dataanalyzer.exe")
    result = subprocess.run([str(entrypoint), "--help"], cwd=tmp_path,
                            capture_output=True, text=True, timeout=15)
    assert result.returncode == 0


def test_cli_one_numeric_column_produces_chart(tmp_path):
    data = tmp_path / "data.csv"
    data.write_text("value\n1\n2\n3\n")
    cli = Path(__file__).parents[1] / "cli.py"
    output = tmp_path / "charts"
    result = subprocess.run([sys.executable, str(cli), "visualize", str(data),
                             "--output", str(output)], capture_output=True, text=True, timeout=30)
    assert result.returncode == 0
    assert list(output.glob("*.png"))

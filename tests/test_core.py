"""Tests for core analyzer."""

import pytest
import pandas as pd
from analyzer.core import Analyzer


@pytest.fixture
def sample_csv(tmp_path):
    df = pd.DataFrame({
        "name": ["Alice", "Bob", "Charlie"],
        "age": [25, 30, 35],
        "salary": [50000, 60000, 70000],
    })
    path = tmp_path / "sample.csv"
    df.to_csv(path, index=False)
    return path


def test_load_csv(sample_csv):
    a = Analyzer(sample_csv)
    assert len(a.df) == 3
    assert list(a.df.columns) == ["name", "age", "salary"]


def test_info(sample_csv):
    a = Analyzer(sample_csv)
    info = a.info()
    assert info["rows"] == 3
    assert len(info["columns"]) == 3


def test_summary(sample_csv):
    a = Analyzer(sample_csv)
    s = a.summary()
    assert "mean" in s.index
    assert "age" in s.columns

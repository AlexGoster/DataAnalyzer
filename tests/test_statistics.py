"""Tests for statistics."""

import pytest
import pandas as pd
from analyzer.statistics import describe_numeric, find_outliers, correlation_matrix


def test_describe_numeric():
    s = pd.Series([1, 2, 3, 4, 5])
    result = describe_numeric(s)
    assert result["mean"] == 3.0
    assert result["median"] == 3.0
    assert result["min"] == 1
    assert result["max"] == 5


def test_find_outliers_iqr():
    s = pd.Series([1, 1, 1, 1, 1, 1, 1, 100])
    outliers = find_outliers(s, method="iqr")
    assert 100 in outliers.values


def test_correlation_matrix():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    corr = correlation_matrix(df)
    assert corr.shape == (2, 2)

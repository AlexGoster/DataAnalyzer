"""Statistical analysis functions."""

import numpy as np
import pandas as pd
from typing import Dict, Any


def describe_numeric(series: pd.Series) -> Dict[str, Any]:
    return {
        "mean": series.mean(),
        "median": series.median(),
        "std": series.std(),
        "min": series.min(),
        "max": series.max(),
        "q25": series.quantile(0.25),
        "q75": series.quantile(0.75),
        "skewness": series.skew(),
        "kurtosis": series.kurtosis(),
    }


def find_outliers(series: pd.Series, method: str = "iqr") -> pd.Series:
    if method == "iqr":
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        return series[(series < lower) | (series > upper)]
    elif method == "zscore":
        z = np.abs((series - series.mean()) / series.std())
        return series[z > 3]
    return pd.Series()


def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    numeric_df = df.select_dtypes(include=[np.number])
    return numeric_df.corr()

"""Data cleaning module."""

import pandas as pd
from typing import Optional


def drop_nulls(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    null_ratio = df.isnull().mean()
    cols_to_drop = null_ratio[null_ratio > threshold].index
    return df.drop(columns=cols_to_drop)


def fill_nulls(df: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
    df = df.copy()
    for col in df.select_dtypes(include="number").columns:
        if strategy == "mean":
            df[col].fillna(df[col].mean(), inplace=True)
        elif strategy == "median":
            df[col].fillna(df[col].median(), inplace=True)
        elif strategy == "zero":
            df[col].fillna(0, inplace=True)
    for col in df.select_dtypes(include="object").columns:
        df[col].fillna("Unknown", inplace=True)
    return df


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()


def convert_types(df: pd.DataFrame, type_map: dict) -> pd.DataFrame:
    df = df.copy()
    for col, dtype in type_map.items():
        if col in df.columns:
            df[col] = df[col].astype(dtype)
    return df

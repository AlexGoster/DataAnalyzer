"""Data cleaning module."""

import pandas as pd
from typing import Optional


def drop_nulls(df: pd.DataFrame, threshold: float = 0.5) -> pd.DataFrame:
    null_ratio = df.isnull().mean()
    cols_to_drop = null_ratio[null_ratio > threshold].index
    return df.drop(columns=cols_to_drop)


def fill_nulls(df: pd.DataFrame, strategy: str = "mean") -> pd.DataFrame:
    if strategy not in ("mean", "median", "zero"):
        raise ValueError("Unknown fill strategy")
    df = df.copy()
    for col in df.select_dtypes(include="number").columns:
        if strategy == "mean":
            df[col] = df[col].fillna(df[col].mean())
        elif strategy == "median":
            df[col] = df[col].fillna(df[col].median())
        elif strategy == "zero":
            df[col] = df[col].fillna(0)
    for col in df.columns:
        if pd.api.types.is_object_dtype(df[col]) or pd.api.types.is_string_dtype(df[col]):
            df[col] = df[col].fillna("Unknown")
    return df


def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    return df.drop_duplicates()


def convert_types(df: pd.DataFrame, type_map: dict) -> pd.DataFrame:
    df = df.copy()
    for col, dtype in type_map.items():
        if col in df.columns:
            df[col] = df[col].astype(dtype)
    return df

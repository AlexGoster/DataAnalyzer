"""Core analyzer class."""

from pathlib import Path
from typing import Optional, Union
import pandas as pd


class Analyzer:
    def __init__(self, filepath: Union[str, Path]):
        self.filepath = Path(filepath)
        self.df: Optional[pd.DataFrame] = None
        self._load()

    def _load(self) -> None:
        suffix = self.filepath.suffix.lower()
        if suffix == ".csv":
            self.df = pd.read_csv(self.filepath)
        elif suffix in (".xlsx", ".xls"):
            self.df = pd.read_excel(self.filepath)
        elif suffix == ".json":
            self.df = pd.read_json(self.filepath)
        else:
            raise ValueError(f"Unsupported format: {suffix}")

    def info(self) -> dict:
        return {
            "rows": len(self.df),
            "columns": list(self.df.columns),
            "dtypes": self.df.dtypes.to_dict(),
            "nulls": self.df.isnull().sum().to_dict(),
            "memory": self.df.memory_usage(deep=True).sum(),
        }

    def head(self, n: int = 5) -> pd.DataFrame:
        return self.df.head(n)

    def summary(self) -> pd.DataFrame:
        return self.df.describe(include="all")

    def select_columns(self, columns: list) -> "Analyzer":
        self.df = self.df[columns]
        return self

    def filter_rows(self, **kwargs) -> "Analyzer":
        for col, value in kwargs.items():
            self.df = self.df[self.df[col] == value]
        return self

    def to_csv(self, output: str) -> Path:
        out = Path(output)
        out.mkdir(parents=True, exist_ok=True)
        path = out / f"{self.filepath.stem}_processed.csv"
        self.df.to_csv(path, index=False)
        return path

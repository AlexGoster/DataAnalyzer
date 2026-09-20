"""Visualization module."""

from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class Visualizer:
    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        sns.set_theme(style="darkgrid")

    def bar_chart(self, df: pd.DataFrame, x: str, y: str, title: str = "") -> Path:
        fig, ax = plt.subplots(figsize=(10, 6))
        df.plot.bar(x=x, y=y, ax=ax)
        ax.set_title(title or f"{y} by {x}")
        path = self.output_dir / f"bar_{x}_{y}.png"
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        return path

    def line_chart(self, df: pd.DataFrame, x: str, y: str, title: str = "") -> Path:
        fig, ax = plt.subplots(figsize=(10, 6))
        df.plot.line(x=x, y=y, ax=ax, marker="o")
        ax.set_title(title or f"{y} over {x}")
        path = self.output_dir / f"line_{x}_{y}.png"
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        return path

    def scatter_plot(self, df: pd.DataFrame, x: str, y: str, title: str = "") -> Path:
        fig, ax = plt.subplots(figsize=(10, 6))
        df.plot.scatter(x=x, y=y, ax=ax, alpha=0.6)
        ax.set_title(title or f"{y} vs {x}")
        path = self.output_dir / f"scatter_{x}_{y}.png"
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        return path

    def heatmap(self, df: pd.DataFrame, title: str = "") -> Path:
        fig, ax = plt.subplots(figsize=(10, 8))
        numeric_df = df.select_dtypes(include="number")
        sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
        ax.set_title(title or "Correlation Heatmap")
        path = self.output_dir / "heatmap.png"
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        return path

    def histogram(self, df: pd.DataFrame, column: str, bins: int = 30) -> Path:
        fig, ax = plt.subplots(figsize=(10, 6))
        df[column].hist(bins=bins, ax=ax, edgecolor="black")
        ax.set_title(f"Distribution of {column}")
        path = self.output_dir / f"hist_{column}.png"
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        return path

    def box_plot(self, df: pd.DataFrame, x: str, y: str) -> Path:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(data=df, x=x, y=y, ax=ax)
        path = self.output_dir / f"box_{x}_{y}.png"
        fig.savefig(path, dpi=150, bbox_inches="tight")
        plt.close(fig)
        return path

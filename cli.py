"""CLI interface for DataAnalyzer."""

import argparse
import sys
from analyzer.core import Analyzer
from analyzer.visualizer import Visualizer
from analyzer.report import ReportGenerator


def cmd_analyze(args):
    a = Analyzer(args.file)
    info = a.info()
    print(f"Rows: {info['rows']}, Columns: {len(info['columns'])}")
    print(f"Columns: {info['columns']}")
    print(f"\nNull values:\n{info['nulls']}")
    print(f"\nSummary:\n{a.summary()}")


def cmd_visualize(args):
    a = Analyzer(args.file)
    v = Visualizer(args.output)
    df = a.df
    numeric_cols = list(df.select_dtypes(include="number").columns[:4])
    if len(numeric_cols) >= 2:
        v.scatter_plot(df, numeric_cols[0], numeric_cols[1])
        v.heatmap(df)
    print(f"Charts saved to {args.output}")


def cmd_report(args):
    a = Analyzer(args.file)
    r = ReportGenerator(args.output)
    path = r.generate(a.df)
    print(f"Report saved to {path}")


def main():
    parser = argparse.ArgumentParser(description="DataAnalyzer CLI")
    subparsers = parser.add_subparsers(dest="command")

    p_analyze = subparsers.add_parser("analyze", help="Analyze dataset")
    p_analyze.add_argument("file", help="Path to data file")
    p_analyze.set_defaults(func=cmd_analyze)

    p_viz = subparsers.add_parser("visualize", help="Generate charts")
    p_viz.add_argument("file", help="Path to data file")
    p_viz.add_argument("--output", default="output", help="Output directory")
    p_viz.set_defaults(func=cmd_visualize)

    p_report = subparsers.add_parser("report", help="Generate HTML report")
    p_report.add_argument("file", help="Path to data file")
    p_report.add_argument("--output", default="report.html", help="Output file")
    p_report.set_defaults(func=cmd_report)

    args = parser.parse_args()
    if args.command:
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

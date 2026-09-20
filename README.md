# DataAnalyzer

Инструмент анализа данных с визуализациями и генерацией отчётов.

## Возможности

- Загрузка CSV, Excel, JSON
- Очистка данных
- Статистический анализ
- Визуализации (matplotlib, seaborn, plotly)
- HTML отчёты
- CLI интерфейс

## Установка

```bash
pip install -r requirements.txt
```

## Использование

```bash
python cli.py analyze data/sales.csv
python cli.py visualize data/sales.csv --output output/
python cli.py report data/sales.csv --output report.html
```

MIT License - AlexGoster


Last updated: 2026-09-20

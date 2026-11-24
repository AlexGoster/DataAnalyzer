# DataAnalyzer

Учебный CLI и Python-модули для анализа таблиц, построения PNG-графиков
и генерации HTML-отчётов. Включён синтетический пример `data/sales.csv`.

## Возможности

- Загрузка CSV и JSON; Excel через pandas и установленные движки.
- Сводная статистика, выбор столбцов, фильтрация и сохранение CSV в Python API.
- Очистка пропусков и дубликатов в `analyzer.cleaner`.
- Гистограммы для числовых столбцов; scatter plot и корреляции при наличии двух.
- HTML-отчёт со статистикой, пропусками и типами столбцов.

PDF-экспорта в CLI нет. Графики создаются отдельной командой и не включаются
автоматически в HTML-отчёт. В Python API есть поиск выбросов по IQR и z-score;
CLI не включает его результаты в отчёт.

## Установка и запуск

Нужен Python 3.11+. Из корня репозитория:

```bash
python -m venv .venv
# Активируйте .venv согласно вашей ОС.
python -m pip install -e .
python cli.py --help
python cli.py analyze data/sales.csv
python cli.py visualize data/sales.csv --output charts
python cli.py report data/sales.csv --output reports/sales.html
```

После установки также доступна команда `dataanalyzer` с теми же аргументами.
Для старого формата `.xls` нужен дополнительный движок `xlrd`;
для `.xlsx` зависимость `openpyxl` уже включена.

## Структура

| Путь | Назначение |
| --- | --- |
| `cli.py` | Команды analyze, visualize, report |
| `analyzer/core.py` | Загрузка и базовые операции над таблицами |
| `analyzer/cleaner.py` | Очистка данных |
| `analyzer/statistics.py` | Статистические функции |
| `analyzer/visualizer.py` | PNG-графики |
| `analyzer/report.py` | HTML-отчёт |
| `tests/` | Тесты и регрессионные сценарии |

## Проверка

```bash
python -m pip install pytest
python -m pytest -o addopts= -q
```

Проверяются синтетические данные, статистика, очистка, HTML и PNG.
Результаты и ограничения предыдущей проверки — в [VERIFICATION.md](VERIFICATION.md).

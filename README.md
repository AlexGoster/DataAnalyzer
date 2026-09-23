# DataAnalyzer

Инструмент для анализа данных, визуализации и генерации отчётов.

## Описание

CLI-приложение на Python для анализа CSV/JSON данных: статистика, графики, отчёты в HTML/PDF.

## Технологии

- **Язык:** Python 3.11+
- **Анализ:** pandas, numpy
- **Визуализация:** matplotlib, seaborn, plotly
- **CLI:** argparse / click
- **Отчёты:** Jinja2, HTML

## Возможности

- Загрузка данных (CSV, JSON, Excel)
- Очистка и нормализация данных
- Статистический анализ (среднее, медиана, стандартное отклонение)
- Визуализация: графики, гистограммы, scatter plots
- Генерация HTML-отчётов
- CLI с параметризацией

## Установка и запуск

```bash
# Клонирование
git clone https://github.com/AlexGoster/DataAnalyzer.git
cd DataAnalyzer

# Установка зависимостей
pip install -r requirements.txt

# Анализ данных
python cli.py analyze data/sales.csv

# Визуализация
python cli.py visualize data/sales.csv --output charts/

# Генерация отчёта
python cli.py report data/sales.csv --output report.html
```

## Примеры команд

```bash
# Базовый анализ
python cli.py analyze data/employees.csv

# Только числовые столбцы
python cli.py analyze data/sales.csv --numeric-only

# Сохранение графиков
python cli.py visualize data/sales.csv --output ./charts --format png

# Полный отчёт
python cli.py report data/customers.csv --output ./reports/customers.html
```

## Структура проекта

```
DataAnalyzer/
├── cli.py               # CLI интерфейс
├── analyzer/            # Логика анализа
│   ├── core.py          # Основной анализ
│   └── statistics.py    # Статистические функции
├── visualizer.py        # Визуализация графиков
├── report.py            # Генерация отчётов
├── cleaner.py           # Очистка данных
├── data/                # Примеры данных
├── tests/               # Тесты
├── setup.py
└── Makefile
```

## Пример отчёта

Отчёт включает:
- Общую информацию о данных
- Статистику по каждому столбцу
- Графики распределения
- Корреляционную матрицу
- Выбросы и аномалии

## Что я изучила

- Работа с pandas для обработки данных
- Визуализация данных (matplotlib, seaborn)
- Проектирование CLI-интерфейсов
- Генерация HTML-отчётов

## License

MIT License - AlexGoster


Last updated: 2026-09-20


Last updated: 2026-09-20


Last updated: 2026-09-20


Last updated: 2026-09-23


Last updated: 2026-09-23

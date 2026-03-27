# 🎬 Kazakhstan Cinema Affordability Analysis

**How many minutes do you need to work to watch a movie in your city?**  
**Сколько минут нужно работать, чтобы посмотреть фильм в своём городе?**

---

## English

### Overview

A personal data project exploring **cinema ticket affordability across Kazakhstan**. We scraped real movie schedules from Kazakhstani cinema websites, enriched the data with average salaries by city, and built an interactive Streamlit dashboard to visualize how many minutes of work it takes to afford a movie ticket — city by city.

### Research Question

> Is cinema equally affordable across Kazakhstan's cities, or does the cost of a ticket represent very different amounts of work depending on where you live?

### Data Collection

- **Web scraping** with Selenium across 10+ Kazakhstani cities (Almaty, Balkhash, Beyneu, Zhanozen, Taraz, Temirtau, Oskemen, and others)
- Data collected across multiple dates (February 2025)
- Merged with **average salary data by city** from public sources
- Key engineered feature: `minutes_needed = (ticket_price / salary_per_hour) * 60`

### Stack

| Tool | Purpose |
|------|---------|
| `Selenium` | Web scraping cinema schedules |
| `pandas` | Data cleaning, merging, feature engineering |
| `openpyxl` | Excel file handling |
| `Streamlit` | Interactive dashboard |
| `Plotly` | Charts and visualizations |

### Dashboard Features

- Average ticket price by city (bar chart)
- Average work time to afford a ticket by city (bar chart)
- City-level drill-down: min/max price, average minutes needed, sample size

### How to Run Locally

```bash
git clone https://github.com/SaniyaBekova/CinemaProject.git
cd CinemaProject
pip install -r requirements.txt
streamlit run streamlit_movie_plotly.py
```

---

## Русский

### О проекте

Пет-проект по анализу **доступности кино в городах Казахстана**. Мы собрали реальное расписание сеансов с сайтов казахстанских кинотеатров, обогатили данные средними зарплатами по городам и построили интерактивный дашборд — чтобы наглядно показать, сколько минут нужно работать, чтобы купить билет в кино, в зависимости от города.

### Вопрос исследования

> Одинаково ли доступно кино в разных городах Казахстана, или стоимость билета означает очень разное количество рабочего времени в зависимости от места проживания?

### Сбор данных

- **Веб-скрапинг** через Selenium по 10+ городам Казахстана (Алматы, Балхаш, Бейнеу, Жанаозен, Тараз, Темиртау, Өскемен и другие)
- Данные собраны за несколько дат (февраль 2025)
- Объединены со **средними зарплатами по городам** из открытых источников
- Ключевая вычисляемая колонка: `minutes_needed = (цена_билета / зарплата_в_час) * 60`

### Технологии

| Инструмент | Назначение |
|-----------|-----------|
| `Selenium` | Скрапинг расписания кинотеатров |
| `pandas` | Очистка данных, объединение, feature engineering |
| `openpyxl` | Работа с Excel файлами |
| `Streamlit` | Интерактивный дашборд |
| `Plotly` | Графики и визуализации |

### Возможности дашборда

- Средняя цена билета по городам (столбчатая диаграмма)
- Среднее время работы для покупки билета по городам
- Детальная информация по выбранному городу: мин/макс цена, среднее время, количество наблюдений

### Запуск локально

```bash
git clone https://github.com/SaniyaBekova/CinemaProject.git
cd CinemaProject
pip install -r requirements.txt
streamlit run streamlit_movie_plotly.py
```

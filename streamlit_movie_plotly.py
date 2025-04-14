
import streamlit as st
import pandas as pd
import plotly.express as px

# Load and clean data
@st.cache_data
def load_data():
    df = pd.read_excel("movie_schedule_with_salary.xlsx")
    df['price_adult'] = df['price_adult'].str.replace(r'[^\d]', '', regex=True).astype(int)
    df['minutes_needed'] = (df['price_adult'] / df['salary_per_hour']) * 60
    df = df.dropna(subset=['price_adult', 'minutes_needed', 'salary_per_hour', 'movie'])
    df = df[df['price_adult'] > 0]
    df = df[df['salary_per_hour'] > 0]
    return df

df = load_data()

# Overall city averages
city_avg_price = df.groupby('city')['price_adult'].mean().reset_index()
city_avg_minutes = df.groupby('city')['minutes_needed'].mean().reset_index()

# Plot 1: Average Ticket Price Across Cities
st.subheader("Средняя цена билета по всем городам")
fig1 = px.bar(city_avg_price, x='city', y='price_adult',
              labels={'city': 'Город', 'price_adult': 'Средняя цена (₸)'},
              title="Средняя цена билета по городам")
st.plotly_chart(fig1)

# Plot 2: Average Work Time to Afford Ticket
st.subheader("Среднее время работы (в минутах), чтобы купить билет")
fig2 = px.bar(city_avg_minutes, x='city', y='minutes_needed',
              labels={'city': 'Город', 'minutes_needed': 'Минуты'},
              title="Сколько минут нужно работать для покупки билета")
st.plotly_chart(fig2)

# City selection for details
st.subheader("Детальная информация по городу")
cities = df['city'].unique()
selected_city = st.selectbox("Выберите город", cities)

# Filter and compute detailed metrics
filtered = df[df['city'] == selected_city]
avg_price = filtered['price_adult'].mean()
avg_minutes = filtered['minutes_needed'].mean()
min_price = filtered['price_adult'].min()
max_price = filtered['price_adult'].max()
sample_size = len(filtered)

# Display summary as text
st.markdown(f'''
**Город:** {selected_city}  
**Средняя цена билета:** {avg_price:.0f} ₸  
**Мин/Макс цена:** {min_price} ₸ / {max_price} ₸  
**Среднее время работы для покупки билета:** {avg_minutes:.1f} минут  
**Количество наблюдений:** {sample_size}
''')

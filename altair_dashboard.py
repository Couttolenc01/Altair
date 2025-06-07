import streamlit as st
import altair as alt
import pandas as pd

df = pd.read_csv('2016-1.csv')

st.title("Dashboard de Felicidad Mundial (2016)")

# Paleta personalizada estilo Pepsi
colores_pepsi = ['#045494', '#ec1434', '#d9d2dc', '#f48494', '#6ca4c4']

# Gráfica de barras por región
bar = alt.Chart(df).mark_bar().encode(
    x='count():Q',
    y=alt.Y('Region:N', sort='-x'),
    color=alt.Color('Region:N', scale=alt.Scale(range=colores_pepsi))
)

st.markdown("## Tablero de Visualización")

col1, col2 = st.columns(2)
with col1:
    st.altair_chart(bar, use_container_width=True)

chart3 = alt.Chart(df).mark_circle(size=100).encode(
    x='Economy (GDP per Capita):Q',
    y='Generosity:Q',
    color=alt.Color('Region:N', scale=alt.Scale(range=colores_pepsi)),
    tooltip=['Country', 'Generosity']
).properties(title="Relación entre economía y generosidad")
with col1:
    st.altair_chart(chart3, use_container_width=True)

chart5 = alt.Chart(df).mark_circle(size=80).encode(
    x='Health (Life Expectancy):Q',
    y='Generosity:Q',
    color=alt.Color('Region:N', scale=alt.Scale(range=colores_pepsi)),
    tooltip=['Country']
).properties(title="Relación entre salud y generosidad")
with col1:
    st.altair_chart(chart5, use_container_width=True)

chart4 = alt.Chart(df).mark_bar().encode(
    x=alt.X('Happiness Score:Q', title='Puntaje de Felicidad'),
    y=alt.Y('Country:N', sort='-x'),
    color=alt.Color('Region:N', scale=alt.Scale(range=colores_pepsi)),
    tooltip=['Happiness Rank']
).properties(title="Top países según su índice de felicidad")
with col2:
    st.altair_chart(chart4, use_container_width=True)

chart7 = alt.Chart(df).mark_boxplot().encode(
    x=alt.X('Region:N'),
    y=alt.Y('Happiness Score:Q'),
    color=alt.Color('Region:N', scale=alt.Scale(range=colores_pepsi))
).properties(title="Distribución del índice de felicidad por región")
with col2:
    st.altair_chart(chart7, use_container_width=True)
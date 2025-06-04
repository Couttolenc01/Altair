import streamlit as st
import altair as alt
import pandas as pd

df = pd.read_csv('2016-1.csv')

st.title("Dashboard de Felicidad Mundial (2016)")

# Selección por Región
click = alt.selection_point(encodings=['color'])

# Paleta personalizada estilo Pepsi
colores_pepsi = ['#045494', '#ec1434', '#d9d2dc', '#f48494', '#6ca4c4']

# Gráfica de barras por región
bar = alt.Chart(df).mark_bar().encode(
    x='count():Q',
    y=alt.Y('Region:N', sort='-x'),
    color=alt.Color('Region:N', scale=alt.Scale(range=colores_pepsi))
).add_params(click)

# Gráfica de dispersión de Economía vs Salud
scatter = alt.Chart(df).mark_circle(size=100).encode(
    x='Economy (GDP per Capita):Q',
    y='Health (Life Expectancy):Q',
    color=alt.condition(click, 'Region:N', alt.value('lightgray')),
    tooltip=['Country', 'Happiness Score']
).transform_filter(click)

# Mostrar ambas gráficas
st.altair_chart(bar & scatter, use_container_width=True)
st.write("Selecciona una región en la barra lateral para filtrar los países en la gráfica de dispersión.")

st.markdown("## Gráfica 3: Economía vs Generosidad")

chart3 = alt.Chart(df).mark_circle(size=100).encode(
    x='Economy (GDP per Capita):Q',
    y='Generosity:Q',
    color=alt.Color('Region:N', scale=alt.Scale(range=colores_pepsi)),
    tooltip=['Country', 'Generosity']
).properties(title="Relación entre economía y generosidad")
st.altair_chart(chart3, use_container_width=True)
st.write("Esta gráfica muestra cómo se relacionan los niveles económicos con la generosidad percibida en cada país. Se utiliza la paleta de colores Pepsi para distinguir las regiones.")


st.markdown("## Gráfica 4: Ranking de Felicidad por País")

chart4 = alt.Chart(df).mark_bar().encode(
    x=alt.X('Happiness Score:Q', title='Puntaje de Felicidad'),
    y=alt.Y('Country:N', sort='-x'),
    color=alt.Color('Region:N', scale=alt.Scale(range=colores_pepsi)),
    tooltip=['Happiness Rank']
).properties(title="Top países según su índice de felicidad")
st.altair_chart(chart4, use_container_width=True)
st.write("Gráfica de barras ordenada que muestra a los países según su índice de felicidad. Ideal para resaltar el ranking global.")

st.markdown("## Gráfica 5: Esperanza de Vida vs Generosidad")

chart5 = alt.Chart(df).mark_circle(size=80).encode(
    x='Health (Life Expectancy):Q',
    y='Generosity:Q',
    color=alt.Color('Region:N', scale=alt.Scale(range=colores_pepsi)),
    tooltip=['Country']
).properties(title="Relación entre salud y generosidad")
st.altair_chart(chart5, use_container_width=True)
st.write("Esta gráfica presenta cómo la salud promedio se asocia con el nivel de generosidad, una relación menos explorada en los gráficos anteriores.")

st.markdown("## Gráfica 6: Score de Felicidad vs Dystopia Residual")

chart6 = alt.Chart(df).mark_circle(size=80).encode(
    x='Dystopia Residual:Q',
    y='Happiness Score:Q',
    color=alt.Color('Region:N', scale=alt.Scale(range=colores_pepsi)),
    tooltip=['Country']
).properties(title="Happiness Score frente a Dystopia Residual")
st.altair_chart(chart6, use_container_width=True)
st.write("El componente de Dystopia Residual ayuda a comparar el efecto 'base' de felicidad, diferenciando mejor a los países más allá de sus métricas objetivas.")

st.markdown("## Gráfica 7: Boxplot de Score de Felicidad por Región")

chart7 = alt.Chart(df).mark_boxplot().encode(
    x=alt.X('Region:N'),
    y=alt.Y('Happiness Score:Q'),
    color=alt.Color('Region:N', scale=alt.Scale(range=colores_pepsi))
).properties(title="Distribución del índice de felicidad por región")
st.altair_chart(chart7, use_container_width=True)
st.write("Esta gráfica de caja permite visualizar la variabilidad y mediana del índice de felicidad dentro de cada región.")

st.markdown("## Gráfica 8 (Interacción dinámica): Click para mostrar salud vs libertad")

click2 = alt.selection_point(encodings=['color'])

chart_base = alt.Chart(df).mark_bar().encode(
    y=alt.Y('Region:N', sort='-x'),
    x='count():Q',
    color=alt.Color('Region:N', scale=alt.Scale(range=colores_pepsi))
).add_params(click2)

chart_detail = alt.Chart(df).mark_circle(size=100).encode(
    x='Health (Life Expectancy):Q',
    y='Freedom:Q',
    color=alt.condition(click2, 'Region:N', alt.value('lightgray')),
    tooltip=['Country']
).transform_filter(click2)

st.altair_chart(chart_base & chart_detail, use_container_width=True)
st.write("Esta interacción dinámica permite seleccionar una región en el gráfico de barras y observar cómo se relaciona la salud con la libertad percibida en los países pertenecientes a dicha región.")
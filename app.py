import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Encabezado
st.header('Exploración de anuncios de venta de coches en EE.UU.')

# Casilla para histograma
if st.checkbox('Mostrar histograma del odómetro'):
    st.write('Histograma del odómetro de los vehículos')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Casilla para scatter plot
if st.checkbox('Mostrar gráfico de dispersión de odómetro vs precio'):
    st.write('Gráfico de dispersión: odómetro vs precio')
    fig2 = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig2, use_container_width=True)


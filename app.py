import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv(r"vehicles_us.csv") #cargamos el dataset

#arreglamos los datos
car_data['model_year'] = car_data['model_year'].fillna(2009) #  Tratamos los valores ausentes en la columna 'model_year'.
car_data['model_year'] = car_data['model_year'].astype('int') #Convertimos la columna 'model_year' de float a int.

vendidos_modelo= car_data.query('days_listed <= 1') [['model_year','model','price']].reset_index() #Creamos un data frame con los datos filtrados que nos interesa graficar.

#Programamos la aplicación
st.header('¡Lo más vendidos!')
hist_button = st.checkbox('Construir un histograma de los carros más vendidos por modelo')
if hist_button:
    st.write('Creación de un histograma para carros más vendidos por modelo, con duráción de máximo 1 día desde la publicación del anuncio.')
    fig = px.histogram(vendidos_modelo, x='model_year')
    st.plotly_chart(fig, use_container_width=True)

hist_button_2 = st.button('Carros más vendidos por referencia')
if hist_button_2:
    st.write('Creación de un histograma para carros más vendidos por referencia, con duráción de máximo 1 día desde la publicación del anuncio.')
    fig_1 = px.histogram(vendidos_modelo, x='model')
    st.plotly_chart(fig_1, use_container_width=True)

chart_button = st.button('Carros más vendidos prelación precio vs referencia')
if chart_button:
    st.write('Creación de un gráfico de dispersión de los carros más vendidos, con duráción de máximo 1 día desde la publicación del anuncio, comparando la relación entre precio y referencia.')
    fig_2 = px.scatter(vendidos_modelo, x='model', y= 'price')
    st.plotly_chart(fig_2, use_container_width=True)
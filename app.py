import pandas as pd
import plotly.express as px
import streamlit as st

st.header("Dashboard de anuncios de coches")

car_data = pd.read_csv("vehicles_us.csv")

st.write("Vista rápida del dataset:")
st.dataframe(car_data.head())

hist_button = st.button("Construir histograma (odometer)")

if hist_button:
    st.write("Histograma del odómetro")
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

scatter_button = st.button("Construir dispersión (odometer vs price)")

if scatter_button:
    st.write("Dispersión: odometer vs price")
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)



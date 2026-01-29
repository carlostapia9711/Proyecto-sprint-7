import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Dashboard de anuncios de coches", layout="centered")

st.header("Dashboard de anuncios de coches")
st.write("Vista rápida del dataset:")

df = pd.read_csv("vehicles_us.csv")
st.dataframe(df.head(10), use_container_width=True)

hist_button = st.button("Construir histograma (odometer)")

if hist_button:
    st.write("Histograma del odómetro")
    fig_hist = px.histogram(df, x="odometer", nbins=50)
    st.plotly_chart(fig_hist, use_container_width=True)

scatter_button = st.button("Construir dispersión (odometer vs price)")

if scatter_button:
    st.write("Relación entre odómetro y precio")
    fig_scatter = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig_scatter, use_container_width=True)


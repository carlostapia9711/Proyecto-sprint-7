import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Dashboard de anuncios de coches", layout="wide")

df = pd.read_csv("vehicles_us.csv")

st.header("Dashboard de anuncios de coches")
st.write("Vista rápida del dataset:")
st.dataframe(df.head(10))

plotly_cfg = {"displayModeBar": False}

if st.button("Construir histograma (odometer)"):
    st.write("Histograma del odómetro")
    fig_hist = px.histogram(df, x="odometer", nbins=50, title="Distribución del odómetro")
    st.plotly_chart(fig_hist, config=plotly_cfg)

if st.button("Construir dispersión (odometer vs price)"):
    st.write("Relación entre odómetro y precio")
    fig_scatter = px.scatter(df, x="odometer", y="price", title="Odómetro vs Precio")
    st.plotly_chart(fig_scatter, config=plotly_cfg)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Pie Chart Keilmuan SKP")

df = pd.read_excel("data_skp.xlsx")

grouped = df.groupby("keilmuan")["JUDUL"].count().reset_index()

labels = grouped["keilmuan"]
values = grouped["JUDUL"]

fig, ax = plt.subplots(figsize=(7,7))
ax.pie(values, labels = labels, autopct='%1.1f', startangle = 90)
ax.set_title("Proporsi Judul Penelitian Berdasarkan Keilmuan")

st.pyplot(fig)

st.subheader("Tabel Data Per Keilmuan")
st.dataframe(grouped)
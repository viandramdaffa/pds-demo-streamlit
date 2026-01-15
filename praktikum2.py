'''
analisa pertemuan 5 tentang 5.Feature Addition.py
'''

import streamlit as st
import pandas as pd

st.title("Cek Judul dan Status SKP")

df = pd.read_excel("data_skp.xlsx")

df["status"] = "Lulus"

df["status_judul"] = df["JUDUL"].apply(
    lambda x : "Judul Kosong" if pd.isnull(x) or x == "" else "Ada Judul"
)

st.subheader("Data SKP")
st.dataframe(df)

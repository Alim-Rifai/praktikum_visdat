# import library yang dibutuhkan
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title("Praktikum 1 - visualisasi data")

st.caption("bagian 2: Data Frame") 

st.markdown("""
1. Jamilatun Khoerunnisa - 0110222254
2. Faiz Abdullah Hanif Firmansyah - 01102222
3. Alim blabla - 01102222
""")

# Dataframe : stuktur data berbentuk tabel (baris dan kolom) yang disediakan oleh li
st.subheader("Data Frame")

df = pd.DataFrame(
np.random.randn(30,10),
columns=('col_no %d' % i for i in range (10))

)

# menampilkan data frame
st.dataframe(df)

# Highlight Nilai minimum
st.subheader("Hightlight Minimum Value di DataFrame")

# hightlight nilai terkecil disetiap kolom dataframe
# axis=0 bekerja per kolom
st.dataframe(df.style.highlight_min(axis=0))

# tabel statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))

)

st.table(df)

# metrics : komponen tampilan angka penting
st.subheader("Metrics")
st.metric(label="Temperature", value="31 C", delta="1.2 C")

col1, col2, col3 = st.columns(3)

# menampilkam indikator data
col1.metric("Curah Hujan", "100 cm", "10 cm") #naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse") #naik tapi buruk
col3.metric(label="pelanggan", value=100, delta=10, delta_color="off")

# menampilkan metrik tambahan dengan nilai kosong atau nol
st.metric(label="speed", value=None, delta=0)   #kosong #naik baik karena di setting default
st.metric("Trees", "91456", "-1132649")#penurunan
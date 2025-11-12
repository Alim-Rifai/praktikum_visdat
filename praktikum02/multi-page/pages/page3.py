import streamlit as st

st.title("📊 Page 3")
st.write("Ini adalah halaman ketiga dari aplikasi multipage Streamlit.")

nama = st.text_input("Masukkan nama kamu:")

if nama:
    st.success(f"Halo {nama}, selamat datang di halaman 3!")
else:
    st.info("Silakan masukkan nama kamu dulu.")

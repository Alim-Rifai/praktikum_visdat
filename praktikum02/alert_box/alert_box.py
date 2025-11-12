import streamlit as st

# Judul
st.title("⚠️ Praktikum 2 - Alert Box")
st.write("Kelompok 2:")
st.markdown("""
- Faiz Abdullah Hanif Firmansyah - 0110222281  
- Jamilatun Khoerunnisa - 0110222254  
- Alim Rifai - 0110122068
""")

st.header("Contoh Penggunaan Alert Box di Streamlit")

# 4 Jenis Alert Box utama
st.info("ℹ️ Ini adalah pesan informasi (st.info)")
st.success("✅ Ini adalah pesan sukses (st.success)")
st.warning("⚠️ Ini adalah pesan peringatan (st.warning)")
st.error("❌ Ini adalah pesan error (st.error)")

st.subheader("💬 Contoh Alert Interaktif")

# Alert berdasarkan input user
nama = st.text_input("Masukkan nama kamu:")

if st.button("Kirim"):
    if nama == "":
        st.warning("⚠️ Nama tidak boleh kosong!")
    else:
        st.success(f"Halo {nama}, data kamu berhasil dikirim!")

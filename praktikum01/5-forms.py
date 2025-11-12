import streamlit as st
import pandas as pd
import datetime

# ============================
# Identitas Kelompok
# ============================
st.title("Praktikum Visualisasi Data - Forms")
st.subheader("Kelompok 2 | Form Input Data")

st.write("""
### 👥 Anggota Kelompok:
- 0110222281 — Faiz Abdullah Hanif Firmansyah  
- 0110222254 — Jamilatun Khoerunnisa  
- 0110122068 — Alim Rifai  
""")

st.write("---")

# ============================
# FORM
# ============================
with st.form("form_praktikum"):
    st.write("### Form Input Pengguna")

    # Text Box
    name = st.text_input("Masukkan Nama Anda")

    # Text Area
    description = st.text_area("Masukkan Deskripsi Diri Anda")

    # Number Input
    age = st.number_input("Masukkan Umur", min_value=1, max_value=100, step=1)

    # Time Input
    time_wakeup = st.time_input("Pilih Jam Bangun Tidur")

    # Date Input
    birth_date = st.date_input("Pilih Tanggal Lahir", value=datetime.date(2000, 1, 1))

    # Color Picker
    favorite_color = st.color_picker("Pilih Warna Favorit", "#00FF00")

    # Dataset Upload (CSV)
    csv_file = st.file_uploader("Upload File CSV", type=["csv"])

    # Submit Button
    submit = st.form_submit_button("Submit")

# ============================
# Output Setelah Submit
# ============================
if submit:
    st.success("Data berhasil dikirim ✅")

    st.write("### 📄 Hasil Input Pengguna")
    st.write(f"**Nama:** {name}")
    st.write(f"**Umur:** {age}")
    st.write(f"**Tanggal Lahir:** {birth_date}")
    st.write(f"**Jam Bangun Tidur:** {time_wakeup}")
    st.write(f"**Warna Favorit:** {favorite_color}")
    st.write("**Deskripsi Diri:**")
    st.write(description)

    # Jika file CSV diupload, tampilkan
    if csv_file is not None:
        st.write(f"**File diupload:** {csv_file.name}")
        df = pd.read_csv(csv_file)
        st.write("### Preview Dataset:")
        st.dataframe(df)
    else:
        st.warning("Tidak ada file CSV yang diupload")

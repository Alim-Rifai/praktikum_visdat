import streamlit as st

# st.markdown() digunakan untuk menampilkan teks dengan format markdown (bullet list, bold, italic, dll.)
st.markdown("""
Kelompok 2:
- Faiz Abdullah Hanif Firmansyah - 0110222281
- Jamilatun Khoerunnisa - 0110222254
- Alim Rifai - 0110122068
""")

# Menampilkan satu gambar
st.write("Displaying an Images")
# Menampilkan gambar dengan menentukan path
st.image("assets/gambar1.jpeg")
# Keterangan sumber gambar
st.write("Image Courtesy: unsplash.com")
# image courtesy
st.write("Displaying Multiple Images")
# Listing out person images
person_images = [
    'assets/gambar1.jpeg',
    'assets/gambar2.jpeg',
    'assets/gambar3.jpeg',
    'assets/gambar4.jpeg',
]

# Menampilkan beberapa gambar dengan lebar 150
st.image(person_images, width=150)
# Keterangan sumber gambar
st.write("Image Courtesy: Unsplash")


# Background Image
import streamlit as st
import base64

# Function to set Image as Background
def add_local_background_image_(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.write("Image Courtesy: unsplash")
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string.decode()});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.write("Background Image")
# Calling Image in function
add_local_background_image_('assets/gambar6.jpeg')

# Resizing an Image
import streamlit as st
from PIL import Image
# Membuka gambar dari path lokal
original_image = Image.open("assets/gambar3.jpeg")
# Menampilkan gambar asli
st.title("Original Image")
st.image(original_image)

# Mengubah ukuran gambar menjadi 600x400
resized_image = original_image.resize((600, 400))
# Menampilkan gambar yang sudah diubah ukurannya
st.title("Resized Image")
st.image(resized_image)


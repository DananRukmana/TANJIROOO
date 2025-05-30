import streamlit as st
import os
import gdown

# Konfigurasi halaman
st.set_page_config(
    page_title="Segarikan",
    page_icon="🐟",
    layout="wide"
)



# Pastikan folder model ada
os.makedirs("model", exist_ok=True)

# Daftar model dan ID Google Drive
model_files = {
    "model/model_cek_ikan.h5": "1MSliz9qsueL4YO5sgc7A69FcpsG7uMQn",
    "model/model_cek_kepala_ikan.h5": "1bUNramVQApA1_cKkbD-5DWOrk_a0AthY",
    "model/model_last_ikan.h5": "1BsCNherYcG7I_DPsYwFJFcrczpbhJSvx"
}

# Download setiap model jika belum ada
for path, file_id in model_files.items():
    if not os.path.exists(path):
        print(f"Mengunduh {path} dari Google Drive...")
        url = f"https://drive.google.com/uc?id={file_id}"
        gdown.download(url, path, quiet=False)

# Tambahan CSS untuk styling
st.markdown("""
    <style>
    .a1 {
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .section-box {
        background-color: #f4f4f4;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 30px;
    }
    .success {
        background-color: #e6ffe6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid green;
        font-size: 18px;
    }
    .error {
        background-color: #ffe6e6;
        padding: 15px;
        border-radius: 10px;
        border-left: 5px solid red;
        font-size: 18px;
    }
    .judul-custom {
        font-size: 38px;
        font-weight: 700;
        margin-top: 10px;
        margin-bottom: 15px;
    }
    .subjudul-custom {
        font-size: 20px;
        color: #555;
        margin-bottom: 25px;
    }
    .hubungi-button {
        display: flex;
        justify-content: center;
        margin-top: 50px;
        margin-bottom: 80px;
    }
    .hubungi-button a {
        background-color: #007BFF;
        color: white;
        padding: 12px 30px;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        font-size: 18px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease;
    }
    .hubungi-button a:hover {
        background-color: #0056b3;
    }
    </style>
""", unsafe_allow_html=True)

# Judul dan deskripsi
st.markdown('<div class="judul-custom">🐟 Segarikan: Sistem Pendeteksi Kesegaran Ikan Untuk Kelayakan Konsumsi Guna Mendukung Keamanan Pangan Berbasis Website</div>', unsafe_allow_html=True)
st.markdown("---")
st.write("""
Selamat datang di aplikasi **Segarikan**.  
Silakan pilih menu di **sidebar kiri** untuk memulai.

Saya harap web ini dapat membantu masyarakat dalam menentukan apakah ikan yang akan dikonsumsi masih **segar** atau **tidak**.  
Jika ada kendala dalam penggunaan, silakan klik tombol **Hubungi** yang ada di bawah halaman ini.
""")

# Tombol biru estetik
st.markdown("""
<div class="hubungi-button">
    <a href="/Kontak" target="_self">📞 Hubungi Kontak</a>
</div>
""", unsafe_allow_html=True)

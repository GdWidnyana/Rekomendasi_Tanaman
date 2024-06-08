import pickle
import numpy as np
import pandas as pd
import streamlit as st
from io import BytesIO

# Memuat model terbaik dari file pickle
with open('model_terbaik.pkl', 'rb') as file:
    model_terbaik = pickle.load(file)

# Memuat selector dari file pickle
with open('selector.pkl', 'rb') as file:
    selector = pickle.load(file)

# Fungsi untuk memprediksi data dari DataFrame
def predict_data(df):
    # Seleksi fitur sesuai dengan model yang disimpan
    selected_features = selector.transform(df)

    # Melakukan prediksi menggunakan model terbaik
    predictions = model_terbaik.predict(selected_features)
    
    # Menambahkan kolom label prediksi ke DataFrame
    df['Label'] = predictions

    return df

# Fungsi untuk menampilkan form input manual dan mendapatkan input dari pengguna
def get_manual_input():
    N = st.number_input("Masukkan nilai N (Nitrogen)", min_value=0.0)
    P = st.number_input("Masukkan nilai P (Phosphorus)", min_value=0.0)
    K = st.number_input("Masukkan nilai K (Potassium)", min_value=0.0)
    temperature = st.number_input("Masukkan nilai temperature (°C)")
    humidity = st.number_input("Masukkan nilai kelembapan", min_value=0.0)
    ph = st.number_input("Masukkan nilai pH", min_value=0.0)
    rainfall = st.number_input("Masukkan nilai curah hujan (mm)", min_value=0.0)
    user_input = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]], 
                            columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    if st.button("Prediksi"):
        predicted_df = predict_data(user_input)
        st.write("Hasil Prediksi:")
        st.write(predicted_df)

# Fungsi untuk menyimpan DataFrame ke dalam format Excel dan mengembalikan bytes-nya
def save_excel(df):
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index=False)
    writer.save()
    excel_bytes = output.getvalue()
    return excel_bytes

# Fungsi untuk menampilkan form input dari file Excel
def get_excel_input():
    uploaded_file = st.file_uploader("Upload file Excel", type=["xlsx"])

    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file)
        return df
    else:
        return None

# Menampilkan judul aplikasi
st.markdown("<h1 style='text-align: center;'>Aplikasi Prediksi Rekomendasi Tanaman</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Final Project Kelompok C3 Pengantar Kecerdasan Buatan</h3>", unsafe_allow_html=True)
st.write("----------------------------------------------------") 
# Memilih metode input (manual atau file Excel)
input_method = st.radio("Pilih Metode Input:", ("Manual", "File Excel"))

if input_method == "Manual":
    # Menampilkan form input manual dan mendapatkan input dari pengguna
    get_manual_input()
else:
    # Mengambil input dari file Excel
    excel_df = get_excel_input()

    if excel_df is not None:
        # Memulai prediksi data dari file Excel
        predicted_df = predict_data(excel_df)

        # Menampilkan hasil prediksi dalam DataFrame di Streamlit
        st.write("Hasil Prediksi:")
        st.write(predicted_df)

        # Tombol untuk mengunduh hasil prediksi dalam file Excel
        excel_bytes = save_excel(predicted_df)
        st.download_button(label="Unduh Hasil Prediksi dalam Excel", data=excel_bytes, 
                           file_name="hasil_prediksi.xlsx", mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    else:
        st.warning("Silakan upload file Excel untuk memprediksi data.")

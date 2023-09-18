import streamlit as st
import requests

# URL layanan web Apps Script
apps_script_url = "https://script.google.com/macros/s/AKfycbySr1hTcrfebDYFzU3XOzPpYcJHnnk9HRx28JuwE_wArHdaWNdXBE8VIOrQKRT5_mII/exec"
# Tampilan Streamlit
st.title("PERTAMBAHAN ASET")
st.write("Masukkan Data:")

# Kolom input
tanggal = st.date_input("Tanggal")
tanggal_str = tanggal.strftime('%Y-%m-%d')
jenis_aset = st.text_input("Jenis Aset")
Jumlah = st.number_input("Jumlah", min_value=0)
Harga = st.number_input("Harga", min_value=0)
total_harga = (Jumlah*Harga)
Keterangan = st.text_input("Keterangan")



if st.button("Kirim Data"):
    # Membangun URL dengan parameter query string
    url = f"{apps_script_url}?tanggal={tanggal_str}&jumlah={Jumlah}&jenis_aset={jenis_aset}&harga={Harga}&total_harga={total_harga}&keterangan={Keterangan}"

    # Mengirim permintaan HTTP GET ke Apps Script
    response = requests.get(url)
    
    if response.status_code == 200:
        st.success("Data berhasil dikirim!")
    else:
        st.error("Terjadi kesalahan saat mengirim data.")

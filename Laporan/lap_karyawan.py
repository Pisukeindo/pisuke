import streamlit as st
import requests
import pandas as pd

def lap_karyawan():
    # Ganti URL dengan URL Google Apps Script Anda
    google_apps_script_url = "https://script.google.com/macros/s/AKfycbx14paFLfnGmvGtwR7-Cbjh5CxPrK9puiC_ofNUnlMH/dev"
    # Mengirim permintaan HTTP ke Apps Script
    response = requests.get(google_apps_script_url)
    
    if response.status_code == 200:
        # Mengonversi data JSON menjadi DataFrame
        data = response.json()
        df = pd.DataFrame(data[1:], columns=data[0])
        return df
    else:
        st.error("Gagal mengambil data dari Google Apps Script.")
        return None

def main():
    st.title("Aplikasi Streamlit untuk Menampilkan Data dari Google Apps Script")

    # Tombol untuk mengambil dan menampilkan data
    if st.button("Tampilkan Data"):
        data = lap_karyawan()
        
        # Jika data berhasil diambil, tampilkan dalam bentuk tabel
        if data is not None:
            st.write(data)

if __name__ == "__main__":
    main()

import streamlit as st
import requests

@st.cache  # Gunakan st.cache untuk menghindari rerun otomatis
def send_data_to_spreadsheet(tanggal, penjualan_pisang_aroma, penjualan_cheese_roll):
    # URL layanan web Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbziM5KXcJV20k5gSC8GbvTW1oj3muhc9abd_XQflBV8rgG0MEKo-ekvuqRxCt-3wk0Z/exec"
    
    # Membangun URL dengan parameter query string
    url = f"{apps_script_url}?tanggal={tanggal}&penjualan_pisang_aroma={penjualan_pisang_aroma}&penjualan_cheese_roll={penjualan_cheese_roll}"
    
    # Mengirim permintaan HTTP GET ke Apps Script
    response = requests.get(url)
    
    return response

def page2():
    # Tampilan Streamlit
    st.title("PENJUALAN HARIAN")
    st.write("Masukkan data:")
    
    # Kolom input
    tanggal = st.date_input("Tanggal")
    penjualan_pisang_aroma = st.number_input("Penjualan Pisang Aroma", min_value=0)
    penjualan_cheese_roll = st.number_input("Penjualan Cheese Roll", min_value=0)
    
    # Tombol untuk mengirim data
    if st.button("Kirim Data"):
        # Verifikasi apakah semua input telah diisi
        if not tanggal or not penjualan_pisang_aroma or not penjualan_cheese_roll:
            st.error("Harap isi semua kolom sebelum mengirim data.")
        else:
            # Kirim data ke spreadsheet
            response = send_data_to_spreadsheet(tanggal, penjualan_pisang_aroma, penjualan_cheese_roll)
            
            if response.status_code == 200:
                st.success("Data berhasil dikirim!")
            else:
                st.error("Terjadi kesalahan saat mengirim data.")

import streamlit as st
import requests

def produksi_harian():
    # URL layanan web Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbyhMXytdktE3emk9c8mPM_rXB4gKI9QZ-q5f9pYmq4yWBu03K1aPg30OGn41-eVqfUeLw/exec"
    # Tampilan Streamlit
    st.write("Masukkan Data:")
    
    # Kolom input
    tanggal = st.date_input("Tanggal")
    tanggal_str = tanggal.strftime('%Y-%m-%d')
    pisang_aroma = st.number_input("Produksi Pisang Aroma", min_value=0)
    cheese_roll = st.number_input("{Produksi Cheese Roll", min_value=0)
    
    
    if st.button("Kirim Data"):
        # Membangun URL dengan parameter query string
        url = f"{apps_script_url}?tanggal={tanggal_str}&pisang_aroma={pisang_aroma}&cheese_roll={jumlah_cheese_roll}"
    
        # Mengirim permintaan HTTP GET ke Apps Script
        response = requests.get(url)
        
        if response.status_code == 200:
            st.success("Data berhasil dikirim!")
        else:
            st.error("Terjadi kesalahan saat mengirim data.")

if __name__ == "__main__":
    produksi_harian()

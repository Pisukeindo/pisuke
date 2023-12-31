import streamlit as st
import requests

def quality_control():
    # URL layanan web Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbzgbjFZYnZGUU1L3JQ3FDPJAjvRo5DX_itajYqcFRsHZ_UORwDbXDwUuRNIukwgYyaOBQ/exec"
    
    # Tampilan Streamlit
    st.write("Masukkan Data:")
    
    # Kolom input
    tanggal = st.date_input("Tanggal")
    tanggal_str = tanggal.strftime('%Y-%m-%d')
    jumlah_pisang_aroma = st.number_input("Jumlah Pisang Aroma", min_value=0)
    keterangan_pisang_aroma = st.text_input("Keterangan Pisang Aroma")
    jumlah_cheese_roll = st.number_input("Jumlah Cheese Roll", min_value=0)
    keterangan_cheese_roll = st.text_input("Keterangan Cheese Roll")
    
    
    if st.button("Kirim Data"):
        # Membangun URL dengan parameter query string
        url = f"{apps_script_url}?tanggal={tanggal_str}&jumlah_pisang_aroma={jumlah_pisang_aroma}&keterangan_pisang_aroma={keterangan_pisang_aroma}&jumlah_cheese_roll={jumlah_cheese_roll}&keterangan_cheese_roll={keterangan_cheese_roll}"
    
        # Mengirim permintaan HTTP GET ke Apps Script
        response = requests.get(url)
        
        if response.status_code == 200:
            st.success("Data berhasil dikirim!")
        else:
            st.error("Terjadi kesalahan saat mengirim data.")

if __name__ == "__main__":
    quality_control()

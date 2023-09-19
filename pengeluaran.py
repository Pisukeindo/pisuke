import streamlit as st
import requests

def page7():
    # URL layanan web Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbxNLNOEH6spI2cGXRcufQ3sFKQUxgQf2F1QFrxtgXNwflEhuFdZy8iHzQM0yntI605t/exec"
    # Tampilan Streamlit
    st.title("PENGELUARAN")
  
    # Kolom input
    sumber = st.text_input("Sumber")
    keterangan = st.text_input("Keterangan")
    jumlah = st.number_input("Jumlah", min_value=0)
    tanggal = st.date_input("Tanggal")
    tanggal_str = tanggal.strftime('%Y-%m-%d')

    if st.button("Kirim Data"):
        # Membangun URL dengan parameter query string
        url = f"{apps_script_url}?sumber={sumber}&keterangan={keterangan}&jumlah={jumlah}&tanggal={tanggal_str}"

        # Mengirim permintaan HTTP GET ke Apps Script
        response = requests.get(url)
        
        if response.status_code == 200:
            st.success("Data berhasil dikirim!")
        else:
            st.error("Terjadi kesalahan saat mengirim data.")

if __name__ == "__main__":
    page7()

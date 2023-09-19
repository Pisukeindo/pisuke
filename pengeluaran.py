import streamlit as st
import requests
import locale

def page7():
    # URL layanan web Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbxNLNOEH6spI2cGXRcufQ3sFKQUxgQf2F1QFrxtgXNwflEhuFdZy8iHzQM0yntI605t/exec"
    # Tampilan Streamlit
    st.title("PENGELUARAN")
  
    # Fungsi untuk mengubah nilai numerik ke format Rupiah
    def format_rupiah(value):
        return locale.currency(value, grouping=True, symbol=None)
    
    # Set lokal untuk format mata uang (Indonesia)
    locale.setlocale(locale.LC_ALL, 'id_ID.UTF-8')

    # Kolom input
    tanggal = st.date_input("Tanggal")
    tanggal_str = tanggal.strftime('%Y-%m-%d')
    sumber = st.text_input("Sumber")
    jumlah = st.number_input("Jumlah (Rupiah)", min_value=0)
    keterangan = st.text_input("Keterangan")

    # Mengubah jumlah menjadi format Rupiah
    jumlah_rupiah = format_rupiah(jumlah)
    
    if st.button("Kirim Data"):
        # Membangun URL dengan parameter query string
        url = f"{apps_script_url}?sumber={sumber}&keterangan={keterangan}&jumlah={jumlah}&tanggal={tanggal_str}"

        # Mengirim permintaan HTTP GET ke Apps Script
        response = requests.get(url)
        
        if response.status_code == 200:
            st.success("Data berhasil dikirim!")
        else:
            st.error("Terjadi kesalahan saat mengirim data.")
    
    # Menampilkan jumlah dalam format Rupiah
    st.write(f"Jumlah (Rupiah): {jumlah_rupiah}")

if __name__ == "__main__":
    page7()

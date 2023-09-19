import streamlit as st
import requests

def page1():
    # URL layanan web Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbxpYPhNgkXi_mDP1zqvdNDMPqEP5ldWLpK5sUY-hzAFQQQ7fBd4Q6x7-mNk5mqx0Xq2bQ/exec"

    # Tampilan Streamlit
    st.title("SUPLIER")
    st.write("Masukkan Data:")

    # Kolom input
    nama_suplier = st.text_input("nama_suplier")
    jenis_barang = st.text_input("jenis_barang")
    kontak = st.text_input("kontak")
    keterangan = st.text_input("keterangan")

    if st.button("Kirim Data"):
        # Membangun URL dengan parameter query string
        url = f"{apps_script_url}?nama_suplier='{nama_suplier}'&jenis_barang='{jenis_barang}'&kontak={kontak}&keterangan='{keterangan}'"

        # Mengirim permintaan HTTP GET ke Apps Script
        response = requests.get(url)
        
        if response.status_code == 200:
            st.success("Data berhasil dikirim!")
        else:
            st.error("Terjadi kesalahan saat mengirim data.")

if __name__ == "__main__":
    page1()

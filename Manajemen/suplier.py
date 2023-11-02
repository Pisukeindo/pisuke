import streamlit as st
import requests

def suplier():
    # URL layanan web Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbwV9P5upUPCVd3mK4i3X8CngIxvoxHhrk_SwnWbqTAjkTHp25j9uTj3yCth6r8jtmcfQg/exec"
    # Tampilan Streamlit
    st.title("SUPLIER")

    # Kolom input
    nama_suplier = st.text_input("Nama Suplier")
    jenis_barang = st.text_input("Jenis Barang")
    kontak = st.text_input("Kontak")
    keterangan = st.text_input("Keterangan")

    if st.button("Kirim Data"):
        # Membangun URL dengan parameter query string
        url = f"{apps_script_url}?nama_suplier={nama_suplier}&jenis_barang={jenis_barang}&kontak={kontak}&keterangan={keterangan}"

        # Mengirim permintaan HTTP GET ke Apps Script
        response = requests.get(url)
        
        if response.status_code == 200:
            st.success("Data berhasil dikirim!")
        else:
            st.error("Terjadi kesalahan saat mengirim data.")

if __name__ == "__main__":
    suplier()
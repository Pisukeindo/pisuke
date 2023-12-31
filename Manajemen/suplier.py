import streamlit as st
import requests

def suplier():
    # URL layanan web Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbw5gkL-bHWXYB8KuLaYaB4MEhM1sLK8nkp47vdcOzAOjbQ9Lwuaqgqa81vhJCegoHWtSw/exec"
    # Tampilan Streamlit
    st.title("SUPLIER")

    # Kolom input
    tanggal = st.date_input("Tanggal")
    tanggal_str = tanggal.strftime('%Y-%m-%d')
    nama_suplier = st.text_input("Nama Suplier")
    jenis_barang = st.text_input("Jenis Barang")
    kontak = st.text_input("Kontak")
    keterangan = st.text_input("Keterangan")

    if st.button("Kirim Data"):
        # Membangun URL dengan parameter query string
        url = f"{apps_script_url}?tanggal={tanggal_str}&nama_suplier={nama_suplier}&jenis_barang={jenis_barang}&kontak={kontak}&keterangan={keterangan}"

        # Mengirim permintaan HTTP GET ke Apps Script
        response = requests.get(url)
        
        if response.status_code == 200:
            st.success("Data berhasil dikirim!")
        else:
            st.error("Terjadi kesalahan saat mengirim data.")

if __name__ == "__main__":
    suplier()

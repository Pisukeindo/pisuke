import streamlit as st
import requests

def page6():

    def format_rupiah(angka):
        angka_str = str(angka)
        ribuan = ""
        n = len(angka_str)
        for i, digit in enumerate(angka_str[::-1]):
            ribuan = digit + ribuan
            if (i + 1) % 3 == 0 and i != n - 1:
                ribuan = "." + ribuan
        return "Gaji: Rp " + ribuan
        
    # URL layanan web Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbzNaLqTormZHk8lz9KEPiWxLUv1xp3-sxEXNELN8ejbNaWWT9O9j7EgkfgoBRfXp9NIvQ/exec"
    # Tampilan Streamlit
    st.title("SUPLIER")
    st.write("Masukkan Data:")

    # Kolom input
    nama = st.text_input("Nama")
    posisi = st.text_input("Posisi")
    kontak = st.text_input("Kontak")
    alamat = st.text_input("Alamat")
    gaji = st.number_input("Gaji", min_value=0)
    jumlah_rupiah = format_rupiah(gaji)
    st.write(f"{jumlah_rupiah}")
    
    tanggal = st.date_input("Tanggal")
    tanggal_str = tanggal.strftime('%Y-%m-%d')

    if st.button("Kirim Data"):
        # Membangun URL dengan parameter query string
        url = f"{apps_script_url}?nama={nama}&posisi={posisi}&kontak={kontak}&alamat={alamat}&gaji={gaji}&tanggal={tanggal_str}"

        # Mengirim permintaan HTTP GET ke Apps Script
        response = requests.get(url)
        
        if response.status_code == 200:
            st.success("Data berhasil dikirim!")
        else:
            st.error("Terjadi kesalahan saat mengirim data.")

if __name__ == "__main__":
    page6()

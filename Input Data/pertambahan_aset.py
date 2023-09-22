import streamlit as st
import requests

def pertambahan_aset():

    def format_rupiah(angka):
        angka_str = str(angka)
        ribuan = ""
        n = len(angka_str)
        for i, digit in enumerate(angka_str[::-1]):
            ribuan = digit + ribuan
            if (i + 1) % 3 == 0 and i != n - 1:
                ribuan = "." + ribuan
        return "Total Harga: Rp " + ribuan
        
    # URL layanan web Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbwKswDrRauvewav1jJ3q5Cp9quz1nkZoLeM_xttRpSIip64lsl2-MPUc8virHge8LI/exec"
    st.title("PERTAMBAHAN ASET")
    st.write("Masukkan Data:")
    
    # Kolom input
    tanggal = st.date_input("Tanggal")
    tanggal_str = tanggal.strftime('%Y-%m-%d')
    jenis_aset = st.text_input("Jenis Aset")
    Jumlah = st.number_input("Jumlah", min_value=0)
    Harga = st.number_input("Harga", min_value=0)
    total_harga = (Jumlah*Harga)
    jumlah_rupiah = format_rupiah(total_harga)
    st.write(f"{jumlah_rupiah}")
    Keterangan = st.text_input("Keterangan")
    
    
    
    if st.button("Kirim Data"):
        # Membangun URL dengan parameter query string
        url = f"{apps_script_url}?tanggal={tanggal_str}&jumlah={Jumlah}&jenis_aset={jenis_aset}&harga={Harga}&total_harga={total_harga}&keterangan={Keterangan}"
    
        # Mengirim permintaan HTTP GET ke Apps Script
        response = requests.get(url)
        
        if response.status_code == 200:
            st.success("Data berhasil dikirim!")
        else:
            st.error("Terjadi kesalahan saat mengirim data.")


if __name__ == "__main__":
    pertambahan_aset()

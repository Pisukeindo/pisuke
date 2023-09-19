import streamlit as st
import requests

def page7():
    # Fungsi untuk mengubah nilai numerik ke format Rupiah
    def format_rupiah(angka):
        angka_str = str(angka)
        ribuan = ""
        n = len(angka_str)
        for i, digit in enumerate(angka_str):
            ribuan = digit + ribuan
            if (i + 1) % 3 == 0 and i != n - 1:
                ribuan = "." + ribuan
        return "Rp " + ribuan

    # URL layanan web Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbxNLNOEH6spI2cGXRcufQ3sFKQUxgQf2F1QFrxtgXNwflEhuFdZy8iHzQM0yntI605t/exec"
    # Tampilan Streamlit
    st.title("PENGELUARAN")

    # Kolom input
    tanggal = st.date_input("Tanggal")
    tanggal_str = tanggal.strftime('%Y-%m-%d')
    sumber = st.text_input("Sumber")
    jumlah = int(st.number_input("Jumlah (Rupiah)", min_value=0))  # Konversi ke int untuk menghilangkan desimal
    jumlah_rupiah = format_rupiah(jumlah)
    st.write(f"Rp {jumlah_rupiah}")
    keterangan = st.text_input("Keterangan")

    # Mengubah jumlah menjadi format Rupiah dengan titik sebagai separator setiap 3 digit
    

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

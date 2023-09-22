import streamlit as st
import requests

def pengeluaran_harian():
    # Fungsi untuk mengubah nilai numerik ke format Rupiah
    def format_rupiah(angka):
        angka_str = str(angka)
        ribuan = ""
        n = len(angka_str)
        for i, digit in enumerate(angka_str[::-1]):
            ribuan = digit + ribuan
            if (i + 1) % 3 == 0 and i != n - 1:
                ribuan = "." + ribuan
        return "Pengeluaran: Rp " + ribuan

    # URL layanan web Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbyLnB24RYOAdjQWWkBdAilXeIf8Ntkb8y4Aba49VFAx4ZtJnCNSRa9ffuBLdglMQcuO/exec"
    # Tampilan Streamlit
    st.title("PENGELUARAN")

    # Kolom input
    tanggal = st.date_input("Tanggal")
    tanggal_str = tanggal.strftime('%Y-%m-%d')
    sumber = st.text_input("Sumber")
    jumlah = int(st.number_input("Jumlah", min_value=0))  
    jumlah_rupiah = format_rupiah(jumlah)
    st.write(f"{jumlah_rupiah}")
    keterangan = st.text_input("Keterangan")

 

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
    pengeluaran_harian()

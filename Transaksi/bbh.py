import streamlit as st
import requests

def page5():
    # URL layanan web Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbw9IFGsHreAqh4qQiRuGnBk_D0G32d3XfhjZjYY5xW_lrUewF3A3-YFbo_U7Kzsi4dw/exec"

    # Tampilan Streamlit
    st.title("BAHAN BAKU HARIAN")

    # Kolom input
    tanggal = st.date_input("Tanggal")
    tanggal_str = tanggal.strftime('%Y-%m-%d')

    # Daftar item
    items = ["keju", "susu", "kulit", "gas", "minyak", "kemasan", "plastik"]

    # Inisialisasi dictionary untuk menyimpan data
    data = {}

    for item in items:
        jumlah = st.number_input(f"Jumlah {item}", min_value=0)
        harga = st.number_input(f"Harga {item}", min_value=0)
        total_pembelian = jumlah * harga
        data[f"jumlah_{item}"] = jumlah
        data[f"harga_{item}"] = harga
        data[f"total_pembelian_{item}"] = total_pembelian

    if st.button("Kirim Data"):
        # Membangun URL dengan parameter query string
        url_params = "&".join([f"{key}={value}" for key, value in data.items()])
        url = f"{apps_script_url}?tanggal={tanggal_str}&{url_params}"

        # Mengirim permintaan HTTP GET ke Apps Script
        response = requests.get(url)

        if response.status_code == 200:
            st.success("Data berhasil dikirim!")
        else:
            st.error("Terjadi kesalahan saat mengirim data.")

if __name__ == "__main__":
   page5()

import streamlit as st
import requests
from datetime import datetime

# URL Google Apps Script yang menghasilkan data JSON
google_apps_script_url = "https://script.google.com/macros/s/AKfycbwMHmmODwrnhdIK_I1XPQjadWwnTqyY0Vb3EHQc3v0LOHYZ3Y1Am14PwgWOaUoDxD8mCw/execc"
# Fungsi untuk mengubah format tanggal menjadi "yyyy-mm-dd"
def format_tanggal(tanggal):
    try:
        # Ubah string tanggal ke dalam objek datetime
        tanggal_obj = datetime.fromisoformat(tanggal)
        # Ubah format tanggal menjadi "yyyy-mm-dd"
        tanggal_formatted = tanggal_obj.strftime('%Y-%m-%d')
        return tanggal_formatted
    except Exception as e:
        # Jika format tanggal tidak valid, coba ekstrak tanggal dari format yang diberikan
        try:
            tanggal_obj = datetime.strptime(tanggal, '%Y-%m-%dT%H:%M:%S.%fZ')
            tanggal_formatted = tanggal_obj.strftime('%Y-%m-%d')
            return tanggal_formatted
        except Exception as e:
            return tanggal  # Kembalikan tanggal asli jika ada kesalahan

# Fungsi untuk mengubah angka menjadi format Rupiah
def format_rupiah(angka):
    try:
        angka_str = "{:,.0f}".format(angka).replace(",", ".")
        return f"Rp {angka_str}"
    except Exception as e:
        return angka  # Kembalikan angka asli jika ada kesalahan

# Fungsi untuk mengambil data dari Google Apps Script
def get_data_from_google_apps_script():
    response = requests.get(google_apps_script_url, params={"sheet": "qc"})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Ganti nama fungsi laporan menjadi lap_qc
def lap_qc():
    data = get_data_from_google_apps_script()

    if data is not None:
        st.title("Filter Data Berdasarkan Tanggal")
        
        # Inisialisasi tanggal terlama dan terbaru
        sheet_values = data[0]['data']
        start_date = end_date = format_tanggal(sheet_values[1][0])

        # Debug: Tambahkan pernyataan berikut untuk mencetak nilai start_date
        st.write(f"start_date: {start_date}")

        # Input tanggal awal dengan validasi rentang waktu
        selected_start_date = st.date_input("Pilih Tanggal Awal", datetime.fromisoformat(start_date))

        # Input tanggal akhir dengan validasi rentang waktu
        selected_end_date = st.date_input("Pilih Tanggal Akhir", datetime.fromisoformat(end_date))

        # Konversi tanggal yang dipilih kembali ke format "yyyy-mm-dd"
        start_date = selected_start_date.strftime('%Y-%m-%d')
        end_date = selected_end_date.strftime('%Y-%m-%d')

        # Tampilkan header
        headers = data[0]['data'][0]
        st.write(headers)

        # Tampilkan data hasil filter
        for row in sheet_values[1:]:
            tanggal_data = format_tanggal(row[0])  # Menggunakan kolom pertama sebagai tanggal
            if start_date <= tanggal_data <= end_date:
                st.write([tanggal_data] + [format_rupiah(float(cell)) if header in kolom_rupiah else cell for header, cell in zip(headers[1:], row[1:])])

if __name__ == "__main__":
    lap_qc()

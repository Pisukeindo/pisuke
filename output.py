import streamlit as st
import requests
import re
from datetime import datetime

# URL Google Apps Script yang menghasilkan data JSON
google_apps_script_url = "https://script.google.com/macros/s/AKfycbwr-2CQmea36435pg0gZJ8Yc686_m5xDxKx66H_8KC-9QOde6bpnHbE4wTyTjTmceda/exec"

# Fungsi untuk mengubah format tanggal menjadi "yyyy-mm-dd"
def format_tanggal(tanggal):
    try:
        # Ubah string tanggal ke dalam objek datetime
        tanggal_obj = datetime.fromisoformat(tanggal)
        # Ubah format tanggal menjadi "yyyy-mm-dd"
        tanggal_formatted = tanggal_obj.strftime('%Y-%m-%d')
        return tanggal_formatted
    except (ValueError, TypeError):
        return tanggal  # Kembalikan tanggal asli jika ada kesalahan

# Fungsi untuk mengubah angka menjadi format Rupiah
def format_rupiah(angka):
    try:
        angka_str = "{:,.0f}".format(angka).replace(",", ".")
        return f"Rp {angka_str}"
    except (ValueError, TypeError):
        return angka  # Kembalikan angka asli jika ada kesalahan

# Fungsi untuk mengambil data dari Google Apps Script sesuai dengan lembar yang diminta
def get_data_from_google_apps_script(selected_sheet):
    response = requests.get(google_apps_script_url, params={"sheet": selected_sheet})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Fungsi filter data berdasarkan kolom dan nilai
def filter_data(sheet_values, filter_column, filter_value):
    filtered_data = []
    headers = sheet_values[0]

    for row in sheet_values[1:]:
        try:
            filter_data = row[headers.index(filter_column)]
            if filter_data == filter_value:
                filtered_data.append(row)
        except (ValueError, TypeError):
            # Jika kolom tidak ada dalam data, abaikan baris ini
            pass

    return filtered_data

# Fungsi hapus filter
def hapus_filter():
    return None, None, None

def laporan(selected_sheet):
    data = get_data_from_google_apps_script(selected_sheet)

    if data is not None:
        for sheet_data in data:
            sheet_name = sheet_data['name']
            sheet_values = sheet_data['data']

            if selected_sheet == sheet_name:
                # Mendapatkan nama-nama kolom yang mengandung "Tanggal", "Bulan", atau "Waktu"
                headers = sheet_values[0]
                kolom_tanggal_bulan_waktu = [header for header in headers if re.search(r"(Tanggal|Bulan|Waktu|tanggal|bulan|waktu)", header, re.IGNORECASE)]

                # Cek apakah lembar memiliki kolom "Tanggal", "Bulan", atau "Waktu"
                if kolom_tanggal_bulan_waktu:
                    st.title(f"Filter Data Berdasarkan Tanggal - Lembar {selected_sheet}")

                    # Tampilkan pilihan Outlet (Pogung, Pandega Mixue, atau Pandega Massiva) jika ini lembar "penjualan_harian"
                    selected_outlet = None
                    if selected_sheet == "penjualan_harian":
                        selected_outlet = st.selectbox("Pilih Outlet", ["Pogung", "Pandega Mixue", "Pandega Massiva"], index=0)

                    # Cari tanggal terlama dan terbaru dalam data
                    all_dates = [format_tanggal(row[headers.index("Tanggal")]) for row in sheet_values[1:]]
                    start_date = min(all_dates)
                    end_date = max(all_dates)

                    # Konversi tanggal terlama dan terbaru ke objek datetime
                    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
                    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

                    # Input tanggal awal dengan validasi rentang waktu
                    selected_start_date = st.date_input("Pilih Tanggal Awal", start_date_obj, min_value=start_date_obj, max_value=end_date_obj)

                    # Input tanggal akhir dengan validasi rentang waktu
                    selected_end_date = st.date_input("Pilih Tanggal Akhir", end_date_obj, min_value=start_date_obj, max_value=end_date_obj)

                    # Tombol hapus filter
                    if st.button("Hapus Filter"):
                        selected_outlet, selected_start_date, selected_end_date = hapus_filter()

                    # Konversi tanggal yang dipilih kembali ke format "yyyy-mm-dd"
                    start_date = selected_start_date.strftime('%Y-%m-%d')
                    end_date = selected_end_date.strftime('%Y-%m-%d')

                    # Filter data berdasarkan tanggal, outlet, dan lembar yang dipilih
                    filtered_data = filter_data(sheet_values, "Tanggal", start_date)
                    filtered_data = filter_data(filtered_data, "Tanggal", end_date)
                    if selected_sheet == "penjualan_harian" and selected_outlet:
                        filtered_data = filter_data(filtered_data, "Outlet", selected_outlet)
                else:
                    # Jika lembar tidak memiliki kolom "Tanggal", "Bulan", atau "Waktu", maka tidak ada filter waktu
                    filtered_data = sheet_values

                # Menampilkan tabel data
                show_table(headers, filtered_data)

if __name__ == "__main__":
    selected_sheet = st.selectbox("Pilih Lembar", ["pengeluaran_Harian", "penjualan_harian"])  # Ganti dengan lembar yang Anda inginkan
    laporan(selected_sheet)

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
    except Exception as e:
        # Jika format tanggal tidak valid, coba ekstrak tanggal dari format yang diberikan
        try:
            tanggal_obj = datetime.strptime(tanggal, '%Y-%m-%dT%H:%M:%S.%fZ')
            tanggal_formatted = tanggal_obj.strftime('%Y-%m-%d')
            return tanggal_formatted
        except Exception as e:
            return tanggal  # Kembalikan tanggal asli jika ada kesalahan

# Fungsi untuk mengambil data dari Google Apps Script sesuai dengan lembar yang diminta
def get_data_from_google_apps_script(selected_sheet):
    response = requests.get(google_apps_script_url, params={"sheet": selected_sheet})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Fungsi untuk menentukan tanggal terlama dan terbaru dalam data lembar
def cari_tanggal_terlama_terbaru(sheet_values, headers):
    tanggal_terlama = datetime.today()
    tanggal_terbaru = datetime(1900, 1, 1)  # Inisialisasi dengan tanggal yang sangat tua

    for row in sheet_values[1:]:
        tanggal_data_str = row[headers.index("Tanggal")]  # Ganti "Tanggal" dengan nama kolom tanggal Anda
        tanggal_data = format_tanggal(tanggal_data_str)
        tanggal_data_obj = datetime.strptime(tanggal_data, '%Y-%m-%d')
        if tanggal_data_obj < tanggal_terlama:
            tanggal_terlama = tanggal_data_obj
        if tanggal_data_obj > tanggal_terbaru:
            tanggal_terbaru = tanggal_data_obj

    return tanggal_terlama, tanggal_terbaru

# Fungsi utama untuk menampilkan laporan dengan filter waktu
def laporan(selected_sheet):
    data = get_data_from_google_apps_script(selected_sheet)

    if data is not None:
        for sheet_data in data:
            sheet_name = sheet_data['name']
            sheet_values = sheet_data['data']

            if selected_sheet == sheet_name:
                headers = sheet_values[0]

                # Cek apakah lembar ini memerlukan filter waktu
                if selected_sheet not in ["suplier", "karyawan"]:
                    tanggal_terlama, tanggal_terbaru = cari_tanggal_terlama_terbaru(sheet_values, headers)

                    konversi_tanggal_dalam_tabel(sheet_values, headers)

                    st.title("Filter Data Berdasarkan Tanggal")
                    start_date = st.date_input("Pilih Tanggal Awal", min_value=tanggal_terlama.date(), max_value=tanggal_terbaru.date(), value=tanggal_terlama.date())
                    end_date = st.date_input("Pilih Tanggal Akhir", min_value=tanggal_terlama.date(), max_value=tanggal_terbaru.date(), value=tanggal_terbaru.date())

                    filtered_data = [headers]
                    for row in sheet_values[1:]:
                        tanggal_data_str = row[headers.index("Tanggal")]  # Ganti "Tanggal" dengan nama kolom tanggal Anda
                        tanggal_data = format_tanggal(tanggal_data_str)
                        if start_date <= datetime.strptime(tanggal_data, '%Y-%m-%d').date() <= end_date:
                            filtered_data.append(row)
                else:
                    filtered_data = sheet_values

                tampilkan_tabel(filtered_data)

# Fungsi untuk menampilkan tabel HTML
def tampilkan_tabel(filtered_data):
    table_html = "<table><tr>"
    for header in filtered_data[0]:
        table_html += f"<th>{header}</th>"
    table_html += "</tr>"
    for row in filtered_data[1:]:
        table_html += "<tr>"
        for cell in row:
            table_html += f"<td>{cell}</td>"
        table_html += "</tr>"
    table_html += "</table>"

    st.markdown(table_html, unsafe_allow_html=True)

if __name__ == "__main__":
    selected_sheet = "pengeluaran_Harian"  # Ganti dengan lembar yang Anda inginkan
    laporan(selected_sheet)

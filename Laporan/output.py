
import streamlit as st
import requests
import re
from datetime import datetime
import pytz

# URL Google Apps Script yang menghasilkan data JSON
google_apps_script_url = "https://script.google.com/macros/s/AKfycbwr-2CQmea36435pg0gZJ8Yc686_m5xDxKx66H_8KC-9QOde6bpnHbE4wTyTjTmceda/exec"

# Fungsi untuk mengubah format tanggal menjadi "yyyy-mm-dd"
def format_tanggal(tanggal):
    try:
        # Ubah string tanggal ke dalam objek datetime
        tanggal_obj = datetime.fromisoformat(tanggal)
        
        # Tetapkan zona waktu Indonesia (WIB)
        zona_waktu_indo = pytz.timezone('Asia/Jakarta')
        tanggal_obj = zona_waktu_indo.localize(tanggal_obj)
        
        # Ubah format tanggal menjadi "yyyy-mm-dd"
        tanggal_formatted = tanggal_obj.strftime('%Y-%m-%d')
        return tanggal_formatted
    except Exception as e:
        # Jika format tanggal tidak valid, coba ekstrak tanggal dari format yang diberikan
        try:
            tanggal_obj = datetime.strptime(tanggal, '%Y-%m-%dT%H:%M:%S.%fZ')
            
            # Tetapkan zona waktu Indonesia (WIB)
            zona_waktu_indo = pytz.timezone('Asia/Jakarta')
            tanggal_obj = zona_waktu_indo.localize(tanggal_obj)
            
            # Ubah format tanggal menjadi "yyyy-mm-dd"
            tanggal_formatted = tanggal_obj.strftime('%Y-%m-%d')
            return tanggal_formatted
        except Exception as e:
            return tanggal  # Kembalikan tanggal asli jika ada kesalahan

def laporan(selected_sheet):
    # Fungsi untuk mengambil data dari Google Apps Script sesuai dengan lembar yang diminta
    def get_data_from_google_apps_script(selected_sheet):
        response = requests.get(google_apps_script_url, params={"sheet": selected_sheet})
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None

    data = get_data_from_google_apps_script(selected_sheet)

    if data is not None:
        for sheet_data in data:
            sheet_name = sheet_data['name']
            sheet_values = sheet_data['data']

            if selected_sheet == sheet_name:
                # Mendapatkan nama-nama kolom
                headers = sheet_values[0]

                # Tampilkan seluruh kolom dalam tabel HTML
                table_html = "<table><tr>"
                for header in headers:
                    table_html += f"<th>{header}</th>"
                table_html += "</tr>"
                for row in sheet_values[1:]:
                    table_html += "<tr>"
                    for cell in row:
                        table_html += f"<td>{cell}</td>"
                    table_html += "</tr>"
                table_html += "</table>"

                # Tampilkan tabel HTML
                st.markdown(table_html, unsafe_allow_html=True)

if __name__ == "__main__":
    selected_sheet = "pengeluaran_Harian"  # Ganti dengan lembar yang Anda inginkan
    laporan(selected_sheet)


def laporan(selected_sheet):
    # Fungsi untuk mengambil data dari Google Apps Script sesuai dengan lembar yang diminta
    def get_data_from_google_apps_script(selected_sheet):
        response = requests.get(google_apps_script_url, params={"sheet": selected_sheet})
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None

    data = get_data_from_google_apps_script(selected_sheet)

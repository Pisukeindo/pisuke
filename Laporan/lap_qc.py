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

def lap_qc(selected_sheet):
    # Fungsi untuk mengambil data dari Google Apps Script sesuai dengan lembar "qc"
    def get_data_from_google_apps_script():
        response = requests.get(google_apps_script_url, params={"sheet": "qc"})
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None

    data = get_data_from_google_apps_script()

    if data is not None:
        for sheet_data in data:
            sheet_name = sheet_data['name']
            sheet_values = sheet_data['data']

            if selected_sheet == sheet_name:
                # Mendapatkan nama-nama kolom yang mengandung "Tanggal", "Bulan", atau "Waktu"
                headers = sheet_values[0]
                kolom_tanggal_bulan_waktu = [header for header in headers if re.search(r"(Tanggal|Bulan|Waktu|tanggal|bulan|waktu)", header, re.IGNORECASE)]

                # Cek apakah lembar "qc" memiliki kolom "Tanggal", "Bulan", atau "Waktu"
                if kolom_tanggal_bulan_waktu:
                    st.title("Filter Data Berdasarkan Tanggal")
                    
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

                    # Konversi tanggal yang dipilih kembali ke format "yyyy-mm-dd"
                    start_date = selected_start_date.strftime('%Y-%m-%d')
                    end_date = selected_end_date.strftime('%Y-%m-%d')

                    # Konversi data tanggal dalam tabel menjadi "yyyy-mm-dd"
                    for i, header in enumerate(headers):
                        if header in kolom_tanggal_bulan_waktu:
                            for j in range(1, len(sheet_values)):
                                sheet_values[j][i] = format_tanggal(sheet_values[j][i])

                    # Filter data berdasarkan tanggal yang dipilih
                    filtered_data = [headers]
                    for row in sheet_values[1:]:
                        try:
                            tanggal_data_str = row[headers.index("Tanggal")]  # Ganti "Tanggal" dengan nama kolom tanggal Anda
                            tanggal_data = format_tanggal(tanggal_data_str)
                            if start_date <= tanggal_data <= end_date:
                                filtered_data.append(row)
                        except ValueError:
                            # Jika kolom "Tanggal" tidak ada dalam data, abaikan baris ini
                            pass
                else:
                    # Jika lembar "qc" tidak memiliki kolom "Tanggal", "Bulan", atau "Waktu", maka tidak ada filter waktu
                    filtered_data = sheet_values

                # Konversi data menjadi format tabel HTML
                table_html = "<table><tr>"
                for header in headers:
                    table_html += f"<th>{header}</th>"
                table_html += "</tr>"
                for row in filtered_data[1:]:
                    table_html += "<tr>"
                    for cell in row:
                        table_html += f"<td>{cell}</td>"
                    table_html += "</tr>"
                table_html += "</table>"

                # Tampilkan tabel HTML
                st.markdown(table_html, unsafe_allow_html=True)

if __name__ == "__main__":
    selected_sheet = "qc"  # Hanya membaca lembar "qc"
    lap_qc(selected_sheet)

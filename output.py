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

# Fungsi untuk mengubah angka menjadi format Rupiah
def format_rupiah(angka):
    try:
        angka_str = "{:,.0f}".format(angka).replace(",", ".")
        return f"Rp {angka_str}"
    except Exception as e:
        return angka  # Kembalikan angka asli jika ada kesalahan

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
                # Mendapatkan nama-nama kolom yang mengandung "Tanggal", "Bulan", atau "Waktu"
                headers = sheet_values[0]
                kolom_tanggal_bulan_waktu = [header for header in headers if re.search(r"(Tanggal|Bulan|Waktu|tanggal|bulan|waktu)", header, re.IGNORECASE)]

                # Tambahkan filter waktu menggunakan widget Streamlit
                st.title("Filter Data Berdasarkan Tanggal")
                start_date = st.date_input("Pilih Tanggal Awal", datetime.today())
                end_date = st.date_input("Pilih Tanggal Akhir", datetime.today())

                # Konversi data tanggal dalam tabel menjadi "yyyy-mm-dd"
                for i, header in enumerate(headers):
                    if header in kolom_tanggal_bulan_waktu:
                        for j in range(1, len(sheet_values)):
                            sheet_values[j][i] = format_tanggal(sheet_values[j][i])

                # Filter data berdasarkan tanggal yang dipilih
                filtered_data = [headers]
                for row in sheet_values[1:]:
                    tanggal_data_str = row[headers.index("Tanggal")]  # Ganti "Tanggal" dengan nama kolom tanggal Anda
                    tanggal_data = format_tanggal(tanggal_data_str)
                    if start_date <= datetime.strptime(tanggal_data, '%Y-%m-%d').date() <= end_date:
                        filtered_data.append(row)

                # Kolom-kolom yang ingin diubah menjadi format Rupiah
                kolom_rupiah = ["Total Pendapatan", "Harga", "Total Harga", "Harga Susu", "Harga Keju", "Harga Kulit", "Harga Gas", "Harga Minyak", "Harga Plastik", "Harga Kemasan", "Gaji", "Jumlah"]

                # Konversi data dalam kolom-kolom tersebut menjadi format Rupiah
                for i, header in enumerate(headers):
                    if header in kolom_rupiah:
                        for j in range(1, len(filtered_data)):
                            filtered_data[j][i] = format_rupiah(float(filtered_data[j][i]))

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

                # Tampilkan

import streamlit as st
import requests
import re
from datetime import datetime

# Fungsi Python untuk mengonversi angka ke huruf
def angka_ke_huruf(teks):
    hasil = ""
    angka_list = teks.split()  # Membagi teks menjadi daftar angka
    for angka_str in angka_list:
        try:
            angka = int(angka_str)
            huruf = chr(angka + 96)  # Mengonversi angka kembali ke huruf
            hasil += huruf
        except ValueError:
            hasil += angka_str  # Jika bukan angka, biarkan seperti itu
    return hasil

# URL Google Apps Script yang menghasilkan data JSON
google_apps_script_url = "https://script.google.com/macros/s/AKfycby7lmAC4eXZQVBhNbcjz2eP_t09PE5jVV5Qnl62ovTS_tpuZg7DTBNjERmZjL2-0vtI/exec"

def laporan(selected_sheet):
    # Fungsi untuk mengambil data dari Google Apps Script
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

                # Kolom yang harus dikonversi kembali ke huruf
                headers_konversi_ke_huruf = ["Nama Suplier", "Jenis Barang", "Keterangan","Jenis Aset", "Keterangan Pisang Aroma", "Keterangan Cheese Roll"]  # Ganti dengan nama kolom yang sesuai
                
                # Konversi nilai tanggal dalam kolom-kolom yang cocok
                for kolom in kolom_tanggal_bulan_waktu:
                    indeks_kolom = headers.index(kolom)
                    for row in sheet_values[1:]:
                        cell = row[indeks_kolom]
                        if cell:  # Pastikan nilai tidak kosong
                            if kolom in headers_konversi_ke_huruf:  # Periksa apakah kolom harus dikonversi
                                # Ubah angka kembali menjadi huruf
                                row[indeks_kolom] = angka_ke_huruf(cell)
                            else:
                                # Ubah format tanggal
                                row[indeks_kolom] = datetime.strptime(cell, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d")

                # Konversi data menjadi format tabel HTML
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
    selected_sheet = "suplier"  # Ganti dengan lembar yang Anda inginkan
    laporan(selected_sheet)

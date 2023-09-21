import streamlit as st
import requests
import re
from datetime import datetime

# URL Google Apps Script yang menghasilkan data JSON
google_apps_script_url = "https://script.google.com/macros/s/AKfycbwr-2CQmea36435pg0gZJ8Yc686_m5xDxKx66H_8KC-9QOde6bpnHbE4wTyTjTmceda/exec"


def filter_data_by_date_range(data, start_date, end_date):
    filtered_data = []

    for row in data:
        try:
            tanggal = datetime.strptime(row, "%Y-%m-%d")
            if start_date <= tanggal <= end_date:
                filtered_data.append(row)
        except ValueError:
            pass

    return filtered_data


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
        # Cek apakah angka bisa diubah menjadi float
        angka_float = float(angka)
        angka_str = "{:,.0f}".format(angka_float).replace(",", ".")
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

# Fungsi utama untuk menampilkan laporan
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

                # Cari indeks kolom dengan tipe waktu terlama dan terbaru
                oldest_date_index = None
                newest_date_index = None

                for i, header in enumerate(headers):
                    if i not in kolom_tanggal_bulan_waktu:
                        continue

                    for value in sheet_values[1:]:
                        try:
                            tanggal = datetime.strptime(value[i], "%Y-%m-%d")
                            if oldest_date_index is None or tanggal < datetime.strptime(sheet_values[1][oldest_date_index], "%Y-%m-%d"):
                                oldest_date_index = i
                            if newest_date_index is None or tanggal > datetime.strptime(sheet_values[1][newest_date_index], "%Y-%m-%d"):
                                newest_date_index = i
                        except ValueError:
                            pass

                if oldest_date_index is not None and newest_date_index is not None:
                    start_date = datetime.strptime(sheet_values[1][oldest_date_index], "%Y-%m-%d")
                    end_date = datetime.strptime(sheet_values[1][newest_date_index], "%Y-%m-%d")
                else:
                    start_date = datetime(2023, 1, 1)
                    end_date = datetime(2023, 12, 31)

                # Tambahkan elemen-elemen UI untuk memasukkan rentang waktu
                st.sidebar.title("Filter Waktu")

                # Input tanggal awal dengan validasi rentang waktu
                start_date = st.sidebar.date_input("Tanggal Awal", start_date, min_value=start_date, max_value=end_date)

                # Input tanggal akhir dengan validasi rentang waktu
                end_date = st.sidebar.date_input("Tanggal Akhir", end_date, min_value=start_date, max_value=end_date)

                # Kolom-kolom yang ingin diubah menjadi format Rupiah
                kolom_rupiah = ["Total Pendapatan", "Harga", "Total Harga", "Harga Susu", "Harga Keju", "Harga Kulit", "Harga Gas", "Harga Minyak", "Harga Plastik", "Harga Kemasan", "Gaji", "Jumlah"]

                # Konversi data dalam kolom-kolom tersebut menjadi format Rupiah
                for i, header in enumerate(headers):
                    if header in kolom_rupiah:
                        for j in range(1, len(sheet_values)):
                            sheet_values[j][i] = format_rupiah(sheet_values[j][i])

                # Konversi data tanggal dalam tabel menjadi "yyyy-mm-dd"
                for i, header in enumerate(headers):
                    if header in kolom_tanggal_bulan_waktu:
                        for j in range(1, len(sheet_values)):
                            sheet_values[j][i] = format_tanggal(sheet_values[j][i])

                # Memfilter data berdasarkan rentang tanggal yang diinput oleh pengguna
                filtered_data = filter_data_by_date_range(sheet_values[1:], start_date, end_date)

                # Konversi data menjadi format tabel HTML
                table_html = "<table><tr>"
                for header in headers:
                    table_html += f"<th>{header}</th>"
                table_html += "</tr>"
                for row in filtered_data:
                    table_html += "<tr>"
                    for cell in row:
                        table_html += f"<td>{cell}</td>"
                    table_html += "</tr>"
                table_html += "</table>"

                # Tampilkan tabel HTML
                st.markdown(table_html, unsafe_allow_html=True)

if __name__ == "__main__":
    st.title("Laporan Data")
    selected_sheet = "pengeluaran_Harian"  # Ganti dengan lembar yang Anda inginkan
    laporan(selected_sheet)

# main.py
import streamlit as st
import requests
import pandas as pd
import re
from datetime import datetime


def laporan_suplier():
    response = requests.get("https://script.google.com/macros/s/AKfycby7lmAC4eXZQVBhNbcjz2eP_t09PE5jVV5Qnl62ovTS_tpuZg7DTBNjERmZjL2-0vtI/exec", params={"sheet": "suplier"})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def laporan_qc():
    response = requests.get("https://script.google.com/macros/s/AKfycby7lmAC4eXZQVBhNbcjz2eP_t09PE5jVV5Qnl62ovTS_tpuZg7DTBNjERmZjL2-0vtI/exec", params={"sheet": "qc"})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def laporan_penjualan_harian():
    response = requests.get("https://script.google.com/macros/s/AKfycby7lmAC4eXZQVBhNbcjz2eP_t09PE5jVV5Qnl62ovTS_tpuZg7DTBNjERmZjL2-0vtI/exec", params={"sheet": "penjualan_harian"})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    st.title("Aplikasi Streamlit untuk Menampilkan Data Google Spreadsheet")

    # Buat menu dropdown untuk memilih lembar
    selected_sheet = st.selectbox("Pilih Lembar:", ["suplier", "qc", "penjualan_harian"])

    if selected_sheet == "suplier":
        data = laporan_suplier()
    elif selected_sheet == "qc":
        data = laporan_qc()
    elif selected_sheet == "penjualan_harian":
        data = laporan_penjualan_harian()
    else:
        data = None

    if data is not None:
        for sheet_data in data:
            sheet_name = sheet_data['name']
            sheet_values = sheet_data['data']

            if selected_sheet == sheet_name:
                st.header(f"Lembar: {sheet_name}")
                st.write("Data dari Google Spreadsheet:")

                # Mendapatkan nama-nama kolom yang mengandung "Tanggal", "Bulan", atau "Waktu"
                headers = sheet_values[0]
                kolom_tanggal_bulan_waktu = [header for header in headers if re.search(r"(Tanggal|Bulan|Waktu|tanggal|bulan|waktu)", header, re.IGNORECASE)]

                # Konversi nilai tanggal dalam kolom-kolom yang cocok
                for kolom in kolom_tanggal_bulan_waktu:
                    indeks_kolom = headers.index(kolom)
                    for row in sheet_values[1:]:
                        cell = row[indeks_kolom]
                        if cell:  # Pastikan nilai tidak kosong
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
    main()

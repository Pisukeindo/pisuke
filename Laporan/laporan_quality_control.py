import streamlit as st
import requests
import re
from datetime import datetime

google_apps_script_url = "https://script.google.com/macros/s/AKfycbw6jvSdbuMj1rFhGPu2smSlcqs6eTLoF5U_Cz4sNvgGw1we09xdI1vJFwxI3lTpI9Tx/exec"



def laporan():
    
    def format_tanggal(tanggal):
    try:
        tanggal_obj = datetime.fromisoformat(tanggal)
        tanggal_formatted = tanggal_obj.strftime('%Y-%m-%d')
        return tanggal_formatted
    except Exception as e:
        try:
            tanggal_obj = datetime.strptime(tanggal, '%Y-%m-%dT%H:%M:%S.%fZ')
            tanggal_formatted = tanggal_obj.strftime('%Y-%m-%d')
            return tanggal_formatted
        except Exception as e:
            return tanggal
            
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

            if "qc" == sheet_name:
                headers = sheet_values[0]
                kolom_tanggal_bulan_waktu = [header for header in headers if re.search(r"(Tanggal|Bulan|Waktu|tanggal|bulan|waktu)", header, re.IGNORECASE)]

                if kolom_tanggal_bulan_waktu:
                    st.title("Filter Data Berdasarkan Tanggal")

                    all_dates = [format_tanggal(row[headers.index("Tanggal")]) for row in sheet_values[1:]]
                    start_date = min(all_dates)
                    end_date = max(all_dates)

                    start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
                    end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")

                    selected_start_date = st.date_input("Pilih Tanggal Awal", start_date_obj, min_value=start_date_obj, max_value=end_date_obj)

                    selected_end_date = st.date_input("Pilih Tanggal Akhir", end_date_obj, min_value=start_date_obj, max_value=end_date_obj)

                    start_date = selected_start_date.strftime('%Y-%m-%d')
                    end_date = selected_end_date.strftime('%Y-%m-%d')

                    for i, header in enumerate(headers):
                        if header in kolom_tanggal_bulan_waktu:
                            for j in range(1, len(sheet_values)):
                                sheet_values[j][i] = format_tanggal(sheet_values[j][i])

                    filtered_data = [headers]
                    for row in sheet_values[1:]:
                        try:
                            tanggal_data_str = row[headers.index("Tanggal")]
                            tanggal_data = format_tanggal(tanggal_data_str)
                            if start_date <= tanggal_data <= end_date:
                                filtered_data.append(row)
                        except ValueError:
                            pass
                else:
                    filtered_data = sheet_values

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

                st.markdown(table_html, unsafe_allow_html=True)

if __name__ == "__main__":
    laporan()

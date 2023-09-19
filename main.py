import streamlit as st
from login import login
from suplier import page1
from quality_control import page2
from penjualan_harian import page3
from pertambahan_aset import page4
from bahan_baku_harian import page5
from karyawan import page6
from output import laporan

# Inisialisasi status login
if "username" not in st.session_state:
    st.session_state.username = None

# Menampilkan halaman sesuai dengan status login
if st.session_state.username is None:
    login()
else:
    selected_menu = st.sidebar.radio(
        "MENU:",
        ["Input Data", "Laporan"]
    )

    if selected_menu == "Input Data":
        selected_page = st.sidebar.radio(
            "Input Data:",
            ["Suplier", "Quality Control", "Penjualan Harian", "Pertambahan Aset", "Bahan Baku Harian", "Karyawan"]
        )

        if selected_page == "Suplier":
            page1()
        elif selected_page == "Quality Control":
            page2()
        elif selected_page == "Penjualan Harian":
            page3()
        elif selected_page == "Pertambahan Aset":
            page4()
        elif selected_page == "Bahan Baku Harian":
            page5()
        elif selected_page == "Karyawan":
            page6()
    
    elif selected_menu == "Laporan":
        selected_laporan = st.sidebar.radio(
            "Laporan:",
            ["Laporan QC", "Laporan Suplier", "Data Karyawan"]  # Ganti dengan nama laporan yang sesuai
        )

        if selected_laporan == "Laporan QC":
            laporan("qc")  # Memanggil fungsi laporan dengan parameter yang sesuai
        elif selected_laporan == "Laporan Suplier":
            laporan("suplier")  # Memanggil fungsi laporan dengan parameter yang sesuai
        elif selected_laporan == "Data Karyawan":
            laporan("karyawan")  # Memanggil fungsi laporan dengan parameter yang sesuai

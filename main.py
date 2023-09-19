import streamlit as st
from login import login
from suplier import page1
from quality_control import page2
from penjualan_harian import page3
from pertambahan_aset import page4
from bahan_baku_harian import page5
from output import laporan

# Inisialisasi status login
if "username" not in st.session_state:
    st.session_state.username = None

# Menampilkan halaman sesuai dengan status login
if st.session_state.username is None:
    login()
else:
    # Sidebar dengan dua menu "PAGE" dan "LAPORAN"
    selected_menu = st.sidebar.radio(
        "Pilih Menu:",
        ["PAGE", "LAPORAN"]
    )

    if selected_menu == "PAGE":
        # Submenu "PAGE" dengan radio button
        selected_page = st.sidebar.radio(
            "Pilih Halaman:",
            ["page1", "page2", "page3", "page4", "page5"]
        )

        if selected_page == "page1":
            page1()
        elif selected_page == "page2":
            page2()
        elif selected_page == "page3":
            page3()
        elif selected_page == "page4":
            page4()
        elif selected_page == "page5":
            page5()
    elif selected_menu == "LAPORAN":
        # Submenu "LAPORAN" dengan radio button
        selected_report = st.sidebar.radio(
            "Pilih Laporan:",
            ["Laporan QC", "Laporan Penjualan"]
        )
        
        if selected_report == "Laporan QC":
            st.title("Laporan Quality Control")
            laporan("qc")
        elif selected_report == "Laporan Penjualan":
            st.title("Laporan Penjualan Harian")
            laporan("penjualan_harian")

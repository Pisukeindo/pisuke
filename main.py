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
    # Radio button untuk memilih "Halaman" atau "Laporan"
    selected_option = st.sidebar.radio(
        "Pilih Menu:",
        ["Halaman", "Laporan"]
    )

    if selected_option == "Halaman":
        # Radio button untuk memilih halaman
        selected_page = st.sidebar.radio(
            "Pilih Halaman:",
            ["Dashboard", "tes"]
        )

        if selected_page == "Dashboard":
            page1()
        elif selected_page == "tes":
            page2()
    else:
        # Radio button untuk memilih jenis laporan
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

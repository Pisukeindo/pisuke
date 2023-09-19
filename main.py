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
    st.sidebar.title("INPUT DATA")

    # Menu "INPUT DATA"
    selected_page = st.sidebar.radio("", ["Penjualan Harian", "Quality Control", "Suplier", "Pertambahan Aset", "Bahan Baku Harian"])
    if selected_page == "Penjualan Harian":
        page3()
    elif selected_page == "Quality Control":
        page2()
    elif selected_page == "Suplier":
        page1()
    elif selected_page == "Pertambahan Aset":
        page4()
    elif selected_page == "Bahan Baku Harian":
        page5()

    st.sidebar.title("LAPORAN")

    # Menu "LAPORAN"
    selected_page = st.sidebar.radio("", ["Laporan QC", "Laporan Penjualan"])
    if selected_page == "Laporan QC":
        st.title("Laporan Quality Control")
        laporan("qc")
    elif selected_page == "Laporan Penjualan":
        st.title("Laporan Penjualan Harian")
        laporan("penjualan_harian")

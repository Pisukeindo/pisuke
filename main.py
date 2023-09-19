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
    # Submenu "INPUT DATA"
    st.sidebar.header("INPUT DATA")
    if st.sidebar.subheader("Penjualan Harian"):
        page3()
    if st.sidebar.button("Quality Control"):
        page2()
    if st.sidebar.button("Suplier"):
        page1()
    if st.sidebar.button("Pertambahan Aset"):
        page4()
    if st.sidebar.button("Bahan Baku Harian"):
        page5()

    # Submenu "LAPORAN"
    st.sidebar.subheader("LAPORAN")
    if st.sidebar.button("Laporan QC"):
        st.title("Laporan Quality Control")
        laporan("qc")
    if st.sidebar.button("Laporan Penjualan"):
        st.title("Laporan Penjualan Harian")
        laporan("penjualan_harian")

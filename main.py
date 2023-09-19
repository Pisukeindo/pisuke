
import streamlit as st
from login import login
from suplier import page1
from quality_control import page2
from penjualan_harian import page3
from pertambahan_aset import page4
from bahan_baku_harian import page5
from output import laporan_qc, laporan_suplier, laporan_penjualan_harian
# Inisialisasi status login
if "username" not in st.session_state:
    st.session_state.username = None

# Menampilkan halaman sesuai dengan status login
if st.session_state.username is None:
    login()
else:
    selected_page = st.sidebar.selectbox("Pilih Halaman:", ["Dashboard", "Suplier", "Quality Control", 
                                                            "Penjualan Harian", "Pertambahan Aset", "Bahan Baku Harian", "Laporan QC", "Laporan Suplier", "Laporan Penjualan Harian"])
    if selected_page == "Dashboard":
        st.write("Ini adalah halaman Dashboard.")
    elif selected_page == "Suplier":
        page1() 
    elif selected_page == "Quality Control":
        page2() 
    elif selected_page == "Penjualan Harian":
        page3() 
    elif selected_page == "Pertambahan Aset":
        page4() 
    elif selected_page == "Bahan Baku Harian":
        page5() 
    elif selected_page == "Laporan QC":
        laporan_qc() 
    elif selected_page == "Laporan Suplier":
        laporan_suplier() 
    elif selected_page == "Laporan Penjualan Harian":
        laporan_penjualan_harian() 



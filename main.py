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

# Inisialisasi status halaman aktif
if "active_page" not in st.session_state:
    st.session_state.active_page = None

# Menampilkan halaman sesuai dengan status login
if st.session_state.username is None:
    login()
else:
    # Tampilkan subheader "PAGE"
    st.sidebar.subheader("PAGE")

    # Submenu "PAGE" dengan radio button
    if st.session_state.active_page != "LAPORAN":
        selected_page = st.sidebar.radio(
            "Pilih Halaman:",
            ["page1", "page2", "page3", "page4", "page5"]
        )

        if selected_page != st.session_state.active_page:
            st.session_state.active_page = selected_page

    # Tampilkan subheader "LAPORAN"
    st.sidebar.subheader("LAPORAN")

    # Submenu "LAPORAN" dengan radio button
    if st.session_state.active_page != "PAGE":
        selected_report = st.sidebar.radio(
            "Pilih Laporan:",
            ["Laporan QC", "Laporan Penjualan"]
        )

        if selected_report != st.session_state.active_page:
            st.session_state.active_page = selected_report

    # Tampilkan halaman atau laporan yang aktif
    if st.session_state.active_page == "page1":
        page1()
    elif st.session_state.active_page == "page2":
        page2()
    elif st.session_state.active_page == "page3":
        page3()
    elif st.session_state.active_page == "page4":
        page4()
    elif st.session_state.active_page == "page5":
        page5()
    elif st.session_state.active_page == "Laporan QC":
        st.title("Laporan Quality Control")
        laporan("qc")
    elif st.session_state.active_page == "Laporan Penjualan":
        st.title("Laporan Penjualan Harian")
        laporan("penjualan_harian")

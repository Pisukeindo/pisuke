import streamlit as st
from login import login
from suplier import page1
from pertambahan_aset import page4
from bahan_baku_harian import page5
from quality_control import page2
from penjualan_harian import page3
from karyawan import page6
from pengeluaran_harian import page7
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
        ["Harian", "Input Data", "Laporan"]
    )

    if selected_menu == "Harian":
        selected_page = st.sidebar.radio(
            "Input Harian:",
            ["Quality Control", "Penjualan Harian", "Bahan Baku Harian", "Pengeluaran Harian"]
        )

        if selected_page == "Quality Control":
            st.title("Quality Control")
            page2()
        elif selected_page == "Penjualan Harian":
            st.title("Penjualan Harian")
            page3()
        elif selected_page == "Bahan Baku Harian":
            st.title("Bahan Baku Harian")
            page5()
        elif selected_page == "Pengeluaran Harian":
            st.title("Pengeluaran Harian")
            page7()

    elif selected_menu == "Input Data":
        selected_page = st.sidebar.radio(
            "Input Data:",
            ["Suplier", "Pertambahan Aset", "Karyawan"]
        )

        if selected_page == "Suplier":
            
            page1()
        elif selected_page == "Pertambahan Aset":
            page4()
        elif selected_page == "Karyawan":
            page6()
        

    elif selected_menu == "Laporan":
        selected_laporan = st.sidebar.radio(
            "Laporan:",
            ["Laporan Quality Control", "Laporan Suplier", "Laporan Karyawan", "Laporan Pertambahan Aset", 
             "Laporan Bahan Baku Harian", "Laporan Stok Bahan Baku", "Laporan Pengeluaran Harian", "Laporan Penjualan Harian"]
        )

        if selected_laporan == "Laporan Quality Control":
            laporan("qc")
        elif selected_laporan == "Laporan Suplier":
            laporan("suplier")
        elif selected_laporan == "Laporan Karyawan":
            laporan("karyawan")
        elif selected_laporan == "Laporan Bahan Baku Harian":
            laporan("bahan_baku_harian")
        elif selected_laporan == "Laporan Stok Bahan Baku":
            laporan("stok_bahan_baku")
        elif selected_laporan == "Laporan pengeluaran Harian":
            laporan("pengeluaran_harian")
        elif selected_laporan == "Laporan Penjualan Harian":
            laporan("penjualan_harian")
        elif selected_laporan == "Laporan Pertambahan Aset":
            laporan("pertambahan_aset")

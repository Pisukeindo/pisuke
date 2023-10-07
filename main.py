import streamlit as st
from log import login
from input import pertambahan_aset,suplier,karyawan
from Transaksi import bahan_baku_harian,quality_control,penjualan_harian,pengeluaran_harian
from Laporan import output, laporan_quality_control

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
            quality_control.page2()
        elif selected_page == "Penjualan Harian":
            st.title("Penjualan Harian")
            penjualan_harian.page3()
        elif selected_page == "Bahan Baku Harian":
            st.title("Bahan Baku Harian")
            bahan_baku_harian.page5()
        elif selected_page == "Pengeluaran Harian":
            st.title("Pengeluaran Harian")
            pengeluaran_harian.page7()

    elif selected_menu == "Input Data":
        selected_page = st.sidebar.radio(
            "Input Data:",
            ["Suplier", "Pertambahan Aset", "Karyawan"]
        )

        if selected_page == "Suplier":
            
            suplier.page1()
        elif selected_page == "Pertambahan Aset":
            pertambahan_aset.page4()
        elif selected_page == "Karyawan":
            karyawan.page6()
        

    elif selected_menu == "Laporan":
        selected_laporan = st.sidebar.radio(
            "Laporan:",
            ["Laporan Quality Control", "Laporan Suplier", "Laporan Karyawan", "Laporan Pertambahan Aset", 
             "Laporan Bahan Baku Harian", "Laporan Stok Bahan Baku", "Laporan Pengeluaran Harian", "Laporan Penjualan Harian"]
        )

        if selected_laporan == "Laporan Quality Control":
            laporan_quality_control.lap_qc()
        elif selected_laporan == "Laporan Suplier":
            output.laporan("suplier")
        elif selected_laporan == "Laporan Karyawan":
            output.laporan("karyawan")
        elif selected_laporan == "Laporan Bahan Baku Harian":
            output.laporan("bahan_baku_harian")
        elif selected_laporan == "Laporan Stok Bahan Baku":
            output.laporan("stok_bahan_baku")
        elif selected_laporan == "Laporan Pengeluaran Harian":
            output.laporan("pengeluaran_harian")
        elif selected_laporan == "Laporan Penjualan Harian":
            output.laporan("penjualan_harian")
        elif selected_laporan == "Laporan Pertambahan Aset":
            output.laporan("pertambahan_aset")

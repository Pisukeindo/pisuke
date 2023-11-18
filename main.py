import streamlit as st
from log import login
from Manajemen import pertambahan_aset,suplier,karyawan
from Harian import bahan_baku_harian,quality_control,penjualan_harian,pengeluaran_harian,produksi_harian
from Laporan import output
# Inisialisasi status login
if "username" not in st.session_state:
    st.session_state.username = None

# Menampilkan halaman sesuai dengan status login
if st.session_state.username is None:
    login()
else:
    selected_menu = st.sidebar.radio(
        "MENU:",
        ["Data Harian", "Data Manajemen", "Laporan Harian", "Laporan Manajemen"]
    )

    if selected_menu == "Data Harian":
        selected_page = st.sidebar.radio(
            "Input Data Harian:",
            ["Quality Control Harian", "Penjualan Harian", "Bahan Baku Harian", "Pengeluaran Harian", "Produksi Harian"]
        )

        if selected_page == "Quality Control Harian":
            st.title("Quality Control")
            quality_control.quality_control()
        elif selected_page == "Penjualan Harian":
            st.title("Penjualan Harian")
            penjualan_harian.penjualan_harian()
        elif selected_page == "Bahan Baku Harian":
            st.title("Bahan Baku Harian")
            bahan_baku_harian.bahan_baku_harian()
        elif selected_page == "Pengeluaran Harian":
            st.title("Pengeluaran Harian")
            pengeluaran_harian.pengeluaran_harian()
        elif selected_page == "Produksi Harian":
            st.title("Produksi Harian")
            produksi_harian.produksi_harian()

    elif selected_menu == "Data Manajemen":
        selected_page = st.sidebar.radio(
            "Input Data Manajemen:",
            ["Suplier", "Pertambahan Aset", "Karyawan"]
        )

        if selected_page == "Suplier":
            
            suplier.suplier()
        elif selected_page == "Pertambahan Aset":
            pertambahan_aset.pertambahan_aset()
        elif selected_page == "Karyawan":
            karyawan.karyawan()
        

    elif selected_menu == "Laporan Harian":
        selected_laporan = st.sidebar.radio(
            "Laporan:",
            ["Laporan Bahan Baku Harian","Laporan Produksi Harian", "Laporan Pengeluaran Harian", "Laporan Penjualan Harian", "Laporan Stok Bahan Baku", "Laporan Quality Control"]
        )

        if selected_laporan == "Laporan Bahan Baku Harian":
            output.laporan("bahan_baku_harian")
        elif selected_laporan == "Laporan Pengeluaran Harian":
            output.laporan("pengeluaran_harian")
        elif selected_laporan == "Laporan Produksi Harian":
            output.laporan("produksi_harian")
        elif selected_laporan == "Laporan Penjualan Harian":
            output.laporan("penjualan_harian")
        elif selected_laporan == "Laporan Stok Bahan Baku":
            output.laporan("stok_bahan_baku")
        elif selected_laporan == "Laporan Quality Control":
            output.laporan("qc")


    elif selected_menu == "Laporan Manajemen":
        selected_laporan = st.sidebar.radio(
            "Laporan:",
            ["Laporan Suplier", "Laporan Karyawan", "Laporan Pertambahan Aset"]
        )

        if selected_laporan == "Laporan Pertambahan Aser":
            output.laporan("Pertambahan Aset")
        elif selected_laporan == "Laporan Suplier":
            output.laporan("suplier")
        elif selected_laporan == "Laporan Karyawan":
            output.laporan("karyawan")
     

import streamlit as st
from bahan_baku_harian import page1
from penjualan_harian import page2
from pertambahan_aset import page3
from quality_control import page4
from suplier import page5

def db():
    # Sidebar dengan pilihan terbaris vertikal
    st.sidebar.title("Menu Navigasi")
    selected_page = st.sidebar.selectbox("Pilih Halaman", ["Halaman 1", "Halaman 2", "Halaman 3"])  # Gantilah dengan nama-nama halaman Anda

    # Tambahkan logika untuk masing-masing halaman di sini
    if selected_page == "Halaman 1":
        page1()
    elif selected_page == "Halaman 2":
        page2()
    elif selected_page == "Halaman 3":
        page3()


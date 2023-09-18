import streamlit as st
from bahan_baku_harian import page1
from penjualan_harian import page2

def db():
    # Sidebar
    st.sidebar.title("Menu Navigasi")
    selected_page = st.sidebar.selectbox(["Halaman Input", "Bahan Baku Harian", "Penjualan Harian"])

    # Judul halaman
    st.title("Dashboard")

    # Halaman Bahan Baku Harian
    if selected_page == "Bahan Baku Harian":
        page1()

    # Halaman Penjualan Harian
    elif selected_page == "Penjualan Harian":
        page2()


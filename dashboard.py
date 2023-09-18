import streamlit as st
from page1 import page1
from page2 import page2

def db():
    # Sidebar
    st.sidebar.title("Menu Navigasi")
    selected_page = st.sidebar.selectbox("Pilih Halaman:", ["Page1", "Page2"])

    # Judul halaman
    st.title("Dashboard")

    # Halaman Page1
    if selected_page == "Page1":
        page1()

    # Halaman Page2
    elif selected_page == "Page2":
        page2()


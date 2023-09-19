# main.py
import streamlit as st
from login import login
from halaman import suplier
from suplier import page1

# Inisialisasi status login
if "username" not in st.session_state:
    st.session_state.username = None

# Menampilkan halaman sesuai dengan status login
if st.session_state.username is None:
    # Halaman login
    st.title("Halaman Login")
    login()  # Panggil fungsi login() untuk menampilkan halaman login
    st.experimental.rerun()
else:
    # Halaman setelah login
    selected_page = st.sidebar.selectbox("Pilih Halaman:", ["Dashboard", "Halaman Lain"])
    if selected_page == "Dashboard":
        st.write("Ini adalah halaman Dashboard.")
    elif selected_page == "Halaman Lain":
        page1()  # Panggil fungsi run_suplier_app() untuk menampilkan halaman suplier

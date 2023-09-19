
import streamlit as st
from login import login
from suplier import page1
from quality_control import page2

# Inisialisasi status login
if "username" not in st.session_state:
    st.session_state.username = None

# Menampilkan halaman sesuai dengan status login
if st.session_state.username is None:
    login()
else:
    selected_page = st.sidebar.selectbox("Pilih Halaman:", ["Dashboard", "Halaman Lain"])
    if selected_page == "Dashboard":
        st.write("Ini adalah halaman Dashboard.")
    elif selected_page == "Halaman Lain":
        page1() 

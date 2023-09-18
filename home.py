import streamlit as st
from login import login
from pages import pages1

# Inisialisasi status login
if "username" not in st.session_state:
    st.session_state.username = None

# Menampilkan halaman sesuai dengan status login
if st.session_state.username is None:
    login()
else:
    selected_page = st.sidebar.selectbox("Pilih Halaman:", ["Dashboard", "Halaman Lain"])
    if selected_page == "Dashboard":
      pages1.page_1()
  

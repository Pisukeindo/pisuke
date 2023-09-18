import streamlit as st
from login import login
from 1.bahan_baku_harian import page1
from 2.penjualan_harian import page2
# Inisialisasi status login
if "username" not in st.session_state:
    st.session_state.username = None

# Menampilkan halaman sesuai dengan status login
if st.session_state.username is None:
    login()
else:
    selected_page = st.sidebar.selectbox("Pilih Halaman:", ["Bahan Baku Harian", "Penjualan Harian"])
    if selected_page == "Bahan Baku Harian":
      page1()
    elif selected_page == "Penjualan Harian":
      page2()
  

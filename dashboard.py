import streamlit as st

def db():
    # Sidebar dengan pilihan terbaris vertikal
    st.sidebar.title("Menu Navigasi")
    selected_page = st.sidebar.radio("Pilih Halaman:", ["Halaman 1", "Halaman 2", "Halaman 3"])  # Gantilah dengan nama-nama halaman Anda

    # Judul halaman
    st.title("Dashboard")

    # Tambahkan logika untuk masing-masing halaman di sini
    if selected_page == "Halaman 1":
        st.write("Ini adalah Halaman 1.")
    elif selected_page == "Halaman 2":
        st.write("Ini adalah Halaman 2.")
    elif selected_page == "Halaman 3":
        st.write("Ini adalah Halaman 3.")

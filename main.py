import streamlit as st
from login_page import login
from data_page import input_data, output_data

st.sidebar.title("Menu")
pages = ["Login", "Halaman Utama", "Input Data", "Output Data"]
choice = st.sidebar.radio("Pilih Halaman", pages)

if choice == "Login":
    login()
elif choice == "Halaman Utama":
    main("admin")  # Gantilah "admin" dengan username yang sudah terautentikasi.
elif choice == "Input Data":
    input_data()
elif choice == "Output Data":
    output_data()

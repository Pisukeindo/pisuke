import streamlit as st
import pandas as pd

def login():
    st.title("Aplikasi Streamlit dengan Fitur Login")

    # Load data akun
    akun = "https://docs.google.com/spreadsheets/d/1Qs5LxFAcYkhVnAk0zAOBAu9FK8KVR8EKhg0Bl27DIk8/export?format=csv"
    account_data = pd.read_csv(akun)

    # Tambahkan input teks untuk username dan password
    username = st.text_input("Username:")
    password = st.text_input("Password:", type='password')

    # Tombol untuk login
    if st.button("Login"):
        if not username or not password:
            st.error("Isi kedua kolom username dan password.")
            return

        # Periksa apakah kombinasi username dan password ada dalam data akun
        user_data = account_data[(account_data['username'] == username) & (account_data['password'] == password)]
        
        if user_data.empty:
            st.error("Login gagal. Cek kembali username dan password Anda.")
        else:
            st.success("Login berhasil! Selamat datang, " + username)
            st.session_state.username = user_data.iloc[0]['username']

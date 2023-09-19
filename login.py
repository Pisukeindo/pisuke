import streamlit as st

# Buat dictionary untuk menyimpan data akun
account_data = {
    'tes': 'tes',
    'user2': 'password2',
    'user3': 'password3'
}

def login():
    st.title("Aplikasi Streamlit dengan Fitur Login")

    # Tambahkan input teks untuk username dan password
    username = st.text_input("Username:")
    password = st.text_input("Password:", type='password')

    # Tombol untuk login
    if st.button("Login"):
        if not username or not password:
            st.error("Isi kedua kolom username dan password.")
            return

        # Periksa apakah kombinasi username dan password ada dalam data akun
        if username in account_data and account_data[username] == password:
            st.success("Login berhasil! Selamat datang, " + username)
            st.session_state.username = username
            st.experimental_rerun()
        else:
            st.error("Login gagal. Cek kembali username dan password Anda.")


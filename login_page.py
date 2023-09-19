import streamlit as st

def authenticate(username, password):
    return username == "admin" and password == "password"

def login():
    st.title("Login")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    login_button = st.button("Login")

    if login_button:
        if authenticate(username, password):
            st.success("Login berhasil!")
        else:
            st.error("Login gagal. Coba lagi.")

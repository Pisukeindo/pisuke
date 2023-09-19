import streamlit as st

def input_data():
    st.title("Halaman Input Data")
    data = st.text_input("Masukkan data:")
    submit_button = st.button("Submit")

    if submit_button:
        # Proses data di sini
        st.success(f"Data berhasil disubmit: {data}")

def output_data():
    st.title("Halaman Output Data")
    # Tampilkan data hasil keluaran di sini

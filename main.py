import streamlit as st
from login import login
from suplier import page1
from quality_control import page2
from penjualan_harian import page3
from pertambahan_aset import page4
from bahan_baku_harian import page5
from output import laporan

# Inisialisasi status login
if "username" not in st.session_state:
    st.session_state.username = None

# Menampilkan halaman sesuai dengan status login
if st.session_state.username is None:
    login()
else:
    selected_page = st.sidebar.radio(
        "Pilih Halaman:",
        ["Dashboard", "tes"],
    )

    if selected_page == "Dashboard":
        page1()
    elif selected_page == "tes":
        page2()

# Tambahkan CSS untuk menghilangkan bullet
st.markdown(
    """
    <style>
    .streamlit-radio-container input[type="radio"] + label::before {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

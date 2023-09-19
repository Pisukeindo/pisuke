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

# Inisialisasi status sidebar
if "show_sidebar" not in st.session_state:
    st.session_state.show_sidebar = True

# Menampilkan halaman sesuai dengan status login
if st.session_state.username is None:
    login()
else:
    if st.session_state.show_sidebar:
        st.sidebar.title("MENU")

        # Submenu "INPUT DATA"
        submenu_input_data = st.sidebar.subheader("INPUT DATA")
        submenu_input_data_options = {
            "Suplier": page1,
            "Quality Control": page2,
            "Penjualan Harian": page3,
            "Pertambahan Aset": page4,
            "Bahan Baku Harian": page5,
        }

        # Submenu "LAPORAN"
        submenu_laporan = st.sidebar.subheader("LAPORAN")
        submenu_laporan_options = {
            "Laporan QC": lambda: laporan("qc"),
            "Laporan Penjualan": lambda: laporan("penjualan_harian"),
        }

        selected_page = None

        for option in submenu_input_data_options:
            if st.sidebar.button(option):
                selected_page = option
                st.session_state.show_sidebar = False  # Menyembunyikan sidebar setelah memilih submenu

        for option in submenu_laporan_options:
            if st.sidebar.button(option):
                selected_page = option
                st.session_state.show_sidebar = False  # Menyembunyikan sidebar setelah memilih submenu

        if selected_page:
            st.title(selected_page)
            if selected_page in submenu_input_data_options:
                submenu_input_data_options[selected_page]()
            elif selected_page in submenu_laporan_options:
                submenu_laporan_options[selected_page]()

    else:
        # Tombol untuk menampilkan kembali sidebar
        if st.button("Tampilkan Sidebar"):
            st.session_state.show_sidebar = True

# Tambahkan CSS untuk menghilangkan persegi di sekitar tombol
st.markdown(
    """
    <style>
    .stButton>button {
        background-color: transparent;
        border: none;
        text-align: left;
        padding: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

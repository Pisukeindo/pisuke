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
    show_sidebar = True  # Tambahkan variabel show_sidebar

    st.sidebar.title("INPUT DATA")
    if st.button("Penjualan Harian", key="penjualan_harian_button"):
        page3()
        show_sidebar = False  # Sematkan show_sidebar saat memilih fitur
    if st.button("Quality Control", key="qc_button"):
        page2()
        show_sidebar = False
    if st.button("Suplier", key="suplier_button"):
        page1()
        show_sidebar = False
    if st.button("Pertambahan Aset", key="pertambahan_aset_button"):
        page4()
        show_sidebar = False
    if st.button("Bahan Baku Harian", key="bahan_baku_harian_button"):
        page5()
        show_sidebar = False

    st.sidebar.title("LAPORAN")
    if st.button("Laporan QC", key="laporan_qc_button"):
        st.title("Laporan Quality Control")
        laporan("qc")
        show_sidebar = False
    if st.button("Laporan Penjualan", key="laporan_penjualan_button"):
        st.title("Laporan Penjualan Harian")
        laporan("penjualan_harian")
        show_sidebar = False

    if show_sidebar:  # Menyembunyikan sidebar jika show_sidebar adalah True
        st.sidebar.empty()

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

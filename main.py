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
    sidebar = st.sidebar
    sidebar.title("MENU")

    # Daftar menu "INPUT DATA"
    input_data_menu = {
        "Penjualan Harian": page3,
        "Quality Control": page2,
        "Suplier": page1,
        "Pertambahan Aset": page4,
        "Bahan Baku Harian": page5,
    }

    # Daftar menu "LAPORAN"
    laporan_menu = {
        "Laporan QC": ("Laporan Quality Control", "qc"),
        "Laporan Penjualan": ("Laporan Penjualan Harian", "penjualan_harian"),
    }

    for label, page_func in input_data_menu.items():
        if sidebar.button(label, key=f"{label}_button"):
            page_func()
            # Tambahkan kode JavaScript untuk menutup sidebar setelah memilih fitur
            sidebar.markdown(
                """
                <script>
                document.getElementsByClassName("sidebar")[0].style.display = "none";
                </script>
                """,
                unsafe_allow_html=True,
            )

    for label, (title, laporan_type) in laporan_menu.items():
        if sidebar.button(label, key=f"{label}_button"):
            st.title(title)
            laporan(laporan_type)
            # Tambahkan kode JavaScript untuk menutup sidebar setelah memilih fitur
            sidebar.markdown(
                """
                <script>
                document.getElementsByClassName("sidebar")[0].style.display = "none";
                </script>
                """,
                unsafe_allow_html=True,
            )

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

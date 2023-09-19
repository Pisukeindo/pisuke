import streamlit as st
from bahan_baku_harian import page1
from penjualan_harian import page2
from pertambahan_aset import page3
from quality_control import page4
from suplier import page5
from  output import output

def db():
    # Sidebar dengan pilihan terbaris vertikal
    st.sidebar.title("Menu Navigasi")
    
    # Menu Input
    st.sidebar.header("Input")
    if st.sidebar.button("Halaman 1"):
        page1()
    if st.sidebar.button("Halaman 2"):
        page2()
    if st.sidebar.button("Halaman 3"):
        page3()
    
    # Menu Output
    st.sidebar.header("Output")
    if st.sidebar.button("Halaman 4"):
        page4()
    if st.sidebar.button("Halaman 5"):
        output()



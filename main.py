import streamlit as st

# Header pada sidebar
st.sidebar.header('Header Sidebar')

# Sub-header pada sidebar
st.sidebar.subheader('Sub-header Sidebar')

# Konten lain pada sidebar
st.sidebar.text('Ini adalah konten lain pada sidebar.')

# Contoh submenu
submenu_expander = st.sidebar.beta_expander("Submenu")
with submenu_expander:
    st.write("Konten submenu pertama")
    st.write("Konten submenu kedua")

import streamlit as st

# Tampilan Streamlit
st.title("PENGELUARAN")

# Kolom input
tanggal = st.date_input("Tanggal")
sumber = st.text_input("Sumber")
jumlah = st.number_input("Jumlah (Rupiah)", min_value=0)
keterangan = st.text_input("Keterangan")

# Menampilkan jumlah dalam format Rupiah secara real-time
st.write(f"Jumlah (Rupiah): {jumlah:,.0f}")

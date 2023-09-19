import streamlit as st
import requests

def page2():
    # URL layanan web Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbziM5KXcJV20k5gSC8GbvTW1oj3muhc9abd_XQflBV8rgG0MEKo-ekvuqRxCt-3wk0Z/exec"
    
    # Tampilan Streamlit
    st.title("PENJUALAN HARIAN")
    st.write("Masukkan data:")
    
    # Kolom input
    tanggal = st.date_input("Tanggal")
    tanggal_str = tanggal.strftime('%Y-%m-%d')
    penjualan_pisang_aroma = st.number_input("Penjualan Pisang Aroma", min_value=0)
    penjualan_cheese_roll = st.number_input("Penjualan Cheese Roll", min_value=0)
    
    # Pesan error jika ada input yang kosong
    if not tanggal or not penjualan_pisang_aroma or not penjualan_cheese_roll:
        st.error("Harap isi semua kolom sebelum mengirim data.")
    else:
        total_pendapatan = ((penjualan_pisang_aroma*1700)+(penjualan_cheese_roll*2000))

        if st.button("Kirim Data"):
            # Membangun URL dengan parameter query string
            url = f"{apps_script_url}?tanggal={tanggal_str}&penjualan_pisang_aroma={penjualan_pisang_aroma}&penjualan_cheese_roll={penjualan_cheese_roll}&total_pendapatan={total_pendapatan}"
        
            # Mengirim permintaan HTTP GET ke Apps Script
            response = requests.get(url)
            
            if response.status_code == 200:
                st.success("Data berhasil dikirim!")
            else:
                st.error("Terjadi kesalahan saat mengirim data.")

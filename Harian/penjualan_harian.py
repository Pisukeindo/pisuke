import streamlit as st
import requests

def penjualan_harian():

    def format_rupiah(angka):
        angka_str = str(angka)
        ribuan = ""
        n = len(angka_str)
        for i, digit in enumerate(angka_str[::-1]):
            ribuan = digit + ribuan
            if (i + 1) % 3 == 0 and i != n - 1:
                ribuan = "." + ribuan
        return "Total Pendapatan: Rp " + ribuan
        
    # URL layanan web Apps Script
    apps_script_url = "https://script.google.com/macros/s/AKfycbz2nXCUxvTQ_9DD8g6_Pd-F52YFJRX0164k69Tcyh67UwAHeaicAlBdlWYalTzxd47C/exec"
    
    # Tampilan Streamlit
    st.title("PENJUALAN HARIAN")
    
    # Kolom input
    tanggal = st.date_input("Tanggal")
    tanggal_str = tanggal.strftime('%Y-%m-%d')
    outlet = st.selectbox("Pilih Outlet", ["Pogung", "Pandega Mixue", "Pandega Massiva"])
    penjualan_pisang_aroma = st.number_input("Penjualan Pisang Aroma", min_value=0)
    penjualan_cheese_roll = st.number_input("Penjualan Cheese Roll", min_value=0)
    total_pendapatan = ((penjualan_pisang_aroma*1700)+(penjualan_cheese_roll*2000))
    jumlah_rupiah = format_rupiah(total_pendapatan)
    st.write(f"{jumlah_rupiah}")
    
    if st.button("Kirim Data"):
        # Membangun URL dengan parameter query string
        url = f"{apps_script_url}?tanggal={tanggal_str}&outlet={outlet}&penjualan_pisang_aroma={penjualan_pisang_aroma}&penjualan_cheese_roll={penjualan_cheese_roll}&total_pendapatan={total_pendapatan}"
    
        # Mengirim permintaan HTTP GET ke Apps Script
        response = requests.get(url)
        
        if response.status_code == 200:
            st.success("Data berhasil dikirim!")
        else:
            st.error("Terjadi kesalahan saat mengirim data.")


if __name__ == "__main__":
    penjualan_harian()

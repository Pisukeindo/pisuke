import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def db():
  # Fungsi untuk menghasilkan data acak
  def generate_data():
      data = {
          'Tanggal': pd.date_range(start='2023-01-01', periods=100),
          'Penjualan': np.random.randint(100, 1000, size=100),
          'Pendapatan': np.random.uniform(1000, 5000, size=100),
      }
      return pd.DataFrame(data)
  
  # Sidebar
  st.sidebar.title("Menu Navigasi")
  page = st.sidebar.selectbox("Pilih Halaman:", ["Beranda", "Data Penjualan", "Grafik Penjualan", "Grafik Pendapatan"])
  
  # Judul halaman
  st.title("Dashboard Penjualan")
  
  # Halaman Beranda
  if page == "Beranda":
      st.write("Selamat datang di Dashboard Penjualan. Silakan pilih halaman di sebelah kiri.")
  
  # Halaman Data Penjualan
  elif page == "Data Penjualan":
      st.header("Data Penjualan")
      data = generate_data()
      st.dataframe(data)
  
  # Halaman Grafik Penjualan
  elif page == "Grafik Penjualan":
      st.header("Grafik Penjualan")
      data = generate_data()
      fig, ax = plt.subplots()
      ax.plot(data['Tanggal'], data['Penjualan'])
      plt.xlabel('Tanggal')
      plt.ylabel('Penjualan')
      st.pyplot(fig)
  
  # Halaman Grafik Pendapatan
  elif page == "Grafik Pendapatan":
      st.header("Grafik Pendapatan")
      data = generate_data()
      fig, ax = plt.subplots()
      ax.plot(data['Tanggal'], data['Pendapatan'])
      plt.xlabel('Tanggal')
      plt.ylabel('Pendapatan')
      st.pyplot(fig)

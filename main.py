import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Analisis Data E-Commerce")
st.write("Analisis data e-commerce dari untuk tugas akhir dari Dicoding")

st.subheader("Performa Pemesanan Tahunan")
order_per_year = pd.read_csv('orders_per_year.csv')

labels = order_per_year['order_purchase_year']
values = order_per_year['order_id']

plt.plot(labels, values, color='skyblue')
plt.title('Rata-rata order per tahun')
plt.xlabel('Tahun')
plt.ylabel('Rata-rata Order')
plt.xticks(ticks=labels)

st.pyplot(plt)

st.subheader("Tipe Pembayaran Paling Banyak Digunakan")
payment_type = pd.read_csv('payment_type.csv')

labels = payment_type['payment_type']
values = payment_type['order_id']

plt.figure(figsize=(10, 6))
plt.bar(labels, values, color='skyblue')
plt.title('Jumlah Pembayaran')
plt.xlabel('Jenis')
plt.ylabel('Jumlah')
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(plt)
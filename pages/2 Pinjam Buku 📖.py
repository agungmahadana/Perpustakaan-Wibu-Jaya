import streamlit as st
import Logic
from datetime import date

st.set_page_config(page_title="Perpustakaan Wibu Jaya", page_icon=":books:")
st.title("Pinjam Buku 📖")
Logic.showTable()
nama = st.sidebar.text_input("Masukkan nama peminjam")
id = st.sidebar.text_input("Masukkan id buku")
jumlah = st.sidebar.number_input("Masukkan jumlah pinjaman", 1)
waktu = st.sidebar.date_input("Masukkan tanggal pengembalian")
nama.lower()
today = date.today()
hasil = waktu - today

if st.sidebar.button("Pinjam"):
    if nama != "":
        if Logic.cekPeminjam(nama) == False:
            Logic.addPeminjam(nama)
        if Logic.cekBuku(id):
            if Logic.cekStok(id) >= jumlah:
                if hasil.days > 30:
                    st.sidebar.error("Maksimal peminjaman adalah 30 hari")
                else:
                    Logic.addTransaksi(nama, id, jumlah, today, waktu)
                    st.sidebar.success("Peminjaman berhasil")
            else:
                st.sidebar.error("Stok buku tidak mencukupi")
        else:
            st.sidebar.error("ID buku tidak ditemukan")
    else:
        st.sidebar.error("Nama tidak boleh kosong")
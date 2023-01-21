import mysql.connector
import pandas as pd
import streamlit as st

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_fp_daa",
)

mycursor = conn.cursor()

def showTable():
    query = "SELECT * FROM data"
    mycursor.execute(query)
    result = mycursor.fetchall()
    df = pd.DataFrame(columns=['ID Buku', 'Judul', 'Jumlah Halaman', 'Tanggal Publikasi', 'Penulis', 'Penerbit', 'Bahasa', 'Rating', 'Stok'])
    for i in result:
        df.loc[len(df)+1] = i
    st.table(df)

def showByTitle(order):
    if order == 'asc':
        query = "SELECT judul FROM data ORDER BY judul ASC"
    elif order == 'desc':
        query = "SELECT judul FROM data ORDER BY judul DESC"
    mycursor.execute(query)
    result = mycursor.fetchall()
    df = pd.DataFrame(columns=['Judul'])
    for i in result:
        df.loc[len(df)+1] = i
    st.table(df)

def showByPages(order):
    if order == 'asc':
        query = "SELECT judul, jml_halaman FROM data ORDER BY jml_halaman ASC"
    elif order == 'desc':
        query = "SELECT judul, jml_halaman FROM data ORDER BY jml_halaman DESC"
    mycursor.execute(query)
    result = mycursor.fetchall()
    df = pd.DataFrame(columns=['Judul', 'Jumlah Halaman'])
    for i in result:
        df.loc[len(df)+1] = i
    st.table(df)

def showByDate(order):
    if order == 'asc':
        query = "SELECT judul, tgl_publikasi FROM data ORDER BY tgl_publikasi ASC"
    elif order == 'desc':
        query = "SELECT judul, tgl_publikasi FROM data ORDER BY tgl_publikasi DESC"
    mycursor.execute(query)
    result = mycursor.fetchall()
    df = pd.DataFrame(columns=['Judul', 'Tanggal Publikasi'])
    for i in result:
        df.loc[len(df)+1] = i
    st.table(df)

def showByAuth(order):
    if order == 'asc':
        query = "SELECT judul, penulis FROM data ORDER BY penulis ASC"
    elif order == 'desc':
        query = "SELECT judul, penulis FROM data ORDER BY penulis DESC"
    mycursor.execute(query)
    result = mycursor.fetchall()
    df = pd.DataFrame(columns=['Judul', 'Penulis'])
    for i in result:
        df.loc[len(df)+1] = i
    st.table(df)

def showByPub(order):
    if order == 'asc':
        query = "SELECT judul, penerbit FROM data ORDER BY penerbit ASC"
    elif order == 'desc':
        query = "SELECT judul, penerbit FROM data ORDER BY penerbit DESC"
    mycursor.execute(query)
    result = mycursor.fetchall()
    df = pd.DataFrame(columns=['Judul', 'Penerbit'])
    for i in result:
        df.loc[len(df)+1] = i
    st.table(df)

def showByLang(order):
    if order == 'asc':
        query = "SELECT judul, bahasa FROM data ORDER BY bahasa ASC"
    elif order == 'desc':
        query = "SELECT judul, bahasa FROM data ORDER BY bahasa DESC"
    mycursor.execute(query)
    result = mycursor.fetchall()
    df = pd.DataFrame(columns=['Judul', 'Bahasa'])
    for i in result:
        df.loc[len(df)+1] = i
    st.table(df)

def showByRating(order):
    if order == 'asc':
        query = "SELECT judul, rating FROM data ORDER BY rating ASC"
    elif order == 'desc':
        query = "SELECT judul, rating FROM data ORDER BY rating DESC"
    mycursor.execute(query)
    result = mycursor.fetchall()
    df = pd.DataFrame(columns=['Judul', 'Rating'])
    for i in result:
        df.loc[len(df)+1] = i
    st.table(df)

def showByStock(order):
    if order == 'asc':
        query = "SELECT judul, stok FROM data ORDER BY stok ASC"
    elif order == 'desc':
        query = "SELECT judul, stok FROM data ORDER BY stok DESC"
    mycursor.execute(query)
    result = mycursor.fetchall()
    df = pd.DataFrame(columns=['Judul', 'Stok'])
    for i in result:
        df.loc[len(df)+1] = i
    st.table(df)

def cekPeminjam(nama):
    query = "SELECT * FROM peminjam WHERE nama = '" + nama + "'"
    mycursor.execute(query)
    result = mycursor.fetchone()
    if result == None:
        return False
    else:
        return result[0]

def addPeminjam(nama):
    query = "INSERT INTO `peminjam` (`nama`) VALUES ('" + nama + "')"
    mycursor.execute(query)
    conn.commit()

def cekBuku(id):
    query = "SELECT id_buku FROM data WHERE id_buku = " + id
    mycursor.execute(query)
    result = mycursor.fetchone()
    return result[0]

def cekStok(id):
    query = "SELECT stok FROM data WHERE id_buku = " + id
    mycursor.execute(query)
    result = mycursor.fetchone()
    return result[0]

def updateStok(id, jumlah):
    jumlah = str(jumlah)
    query = "UPDATE data SET stok = stok-" + jumlah + " WHERE id_buku = " + id
    mycursor.execute(query)
    conn.commit()

def addTransaksi(nama, buku, jml, tgl, tgl_kembali):
    nama = str(cekPeminjam(nama))
    jml = str(jml)
    tgl = str(tgl)
    tgl_kembali = str(tgl_kembali)
    awal = str(cekStok(buku))
    akhir = str(cekStok(buku) - int(jml))
    updateStok(buku, jml)
    query = "INSERT INTO `transaksi` (`id_peminjam`, `id_buku`, `jml_pinjaman`, `stok_awal`, `stok_akhir`, `tgl_transaksi`, `tgl_pengembalian`) VALUES ('" + nama + "', '" + buku + "', '" + jml + "', '" + awal + "', '" + akhir + "', '" + tgl + "', '" + tgl_kembali + "')"
    mycursor.execute(query)
    conn.commit()
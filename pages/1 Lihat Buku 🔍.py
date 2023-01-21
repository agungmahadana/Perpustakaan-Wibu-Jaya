import streamlit as st
import Logic

st.set_page_config(page_title="Perpustakaan Wibu Jaya", page_icon=":books:")
st.title("Lihat Buku 🔍")
kategori = st.sidebar.selectbox("Pilih kategori", ["Judul", "Jumlah Halaman", "Tanggal Publikasi", "Penulis", "Penerbit", "Bahasa", "Rating", "Stok"])
urutan = st.sidebar.radio("Urutkan", ["Ascending", "Descending"])

if kategori == 'Judul' and urutan == 'Ascending':
    Logic.showByTitle('asc')
elif kategori == 'Judul' and urutan == 'Descending':
    Logic.showByTitle('desc')

elif kategori == 'Jumlah Halaman' and urutan == 'Ascending':
    Logic.showByPages('asc')
elif kategori == 'Jumlah Halaman' and urutan == 'Descending':
    Logic.showByPages('desc')

elif kategori == 'Tanggal Publikasi' and urutan == 'Ascending':
    Logic.showByDate('asc')
elif kategori == 'Tanggal Publikasi' and urutan == 'Descending':
    Logic.showByDate('desc')

elif kategori == 'Penulis' and urutan == 'Ascending':
    Logic.showByAuth('asc')
elif kategori == 'Penulis' and urutan == 'Descending':
    Logic.showByAuth('desc')

elif kategori == 'Penerbit' and urutan == 'Ascending':
    Logic.showByPub('asc')
elif kategori == 'Penerbit' and urutan == 'Descending':
    Logic.showByPub('desc')

elif kategori == 'Bahasa' and urutan == 'Ascending':
    Logic.showByLang('asc')
elif kategori == 'Bahasa' and urutan == 'Descending':
    Logic.showByLang('desc')

elif kategori == 'Rating' and urutan == 'Ascending':
    Logic.showByRating('asc')
elif kategori == 'Rating' and urutan == 'Descending':
    Logic.showByRating('desc')

elif kategori == 'Stok' and urutan == 'Ascending':
    Logic.showByStock('asc')
elif kategori == 'Stok' and urutan == 'Descending':
    Logic.showByStock('desc')
import streamlit as st
import math

#halaman utama
st.title ('aplikasi perhitungan luas bangun datar')
st.header('buatan anak sistem informasi')

menu = st.sidebar.selectbox('Menu', ['luas persegi','luas segitiga','luas lingkaran'])
if menu == 'luas persegi':
    st.write('halaman untuk menghitung luas persegi')
    st.image('https://awsimages.detik.net.id/community/media/visual/2022/11/09/keliling-persegi_169.jpeg?w=600&q=90', caption='gambar persegi')
    sisi = st.number_input('silahkan masukan sisi', min_value=0,)
    if st.button('hitung'):
        luas = sisi * sisi
        st.write(f'luas persegi adalah {luas}')
    
    
elif menu == 'luas segitiga':
    st.write('halaman untuk menghitung luas segitiga')
    st.image('https://asset-a.grid.id/crop/0x0:0x0/700x0/photo/2020/04/27/2008777398.jpg', caption='gambar segitiga')
    alas = st.number_input('silahkan masukan alas', min_value=0)
    tinggi = st.number_input('silahkan masukan tinggi', min_value=0)
    if st.button('hitung'):
        luas = (alas * tinggi) / 2
        st.write(f'luas segitiga adalah {luas}')
        
elif menu == 'luas lingkaran':
    st.write('halaman untuk menghitung luas lingkaran')
    st.image('https://1.bp.blogspot.com/-B-a-CMAY6SQ/X3EroJJd6UI/AAAAAAAAUBM/zdC5ObY7F8o-EOYBV_zenNkaDRJYeuyjACLcBGAsYHQ/s800/jari-jari-lingkaran.jpg', caption='gambar lingkaran')
    r = st.number_input('silahkan masukan jari-jari', min_value=0)
    
    if st.button('hitung'):
        luas = math.pi * r * r
        st.write(f'luas lingkaran adalah {luas:.2f}')
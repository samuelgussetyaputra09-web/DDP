def Lpersegi (sisi):
    return sisi * sisi
def Lsegitiga (alas, tinggi):
    return 0.5 * alas * tinggi
def Llingkaran (jari_jari):
    return 3.14 * jari_jari * jari_jari
def Ljajar_genjang (alas, tinggi):
    return alas * tinggi
def Lpersegi_panjang (panjang, Lebar):
    return panjang * Lebar
                

print(Lpersegi_panjang(3,6))
print(Lsegitiga(3,3))
print(Llingkaran(14))
print(Ljajar_genjang(3,3))
print(Lpersegi_panjang(8,9))

def Kpersegi (sisi):
    return 4 * sisi
def Ksegitiga (sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3
def Klingkaran (jari_jari):
    return 2 * 3.14 * jari_jari
def Kjajaran_genjang (sisi1, sisi2):
    return 2 * (sisi1 + sisi2)
def Kpersegi_panjang (panjang, Lebar):
    return 2 * (panjang+Lebar)
                

print(Kpersegi(8))
print(Ksegitiga(5,5,5))
print(Klingkaran(14))
print(Kjajaran_genjang(3,3))
print(Kpersegi_panjang(3,8))

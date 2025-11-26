import math
def kubus (sisi):
    hasil = math.pow(sisi, 3)
    return hasil


def balok(p,l,t):
    hasil = p * l * t
    return hasil

def prisma(alas, tinggi_segitiga, tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_segitiga
    hasil = luas_alas * tinggi_prisma
    return hasil

def Lkerucut(r, t):
    return (1/3) * 3.14 * r * r * t

def Ltabung(r, t):
    return 3.14 * r * r * t


print(prisma(3,3,3))
print(balok(3,3,3)) 
print(kubus(3))
print(Lkerucut(7,8))
print(Ltabung(7,7))
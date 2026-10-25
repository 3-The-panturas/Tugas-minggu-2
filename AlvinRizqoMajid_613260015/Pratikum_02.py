# =========================================
# PRAKTIKUM 2: BILANGAN PRIMA & BREAK
# =========================================

def cek_prima(angka):
    is_prima = True  # Flag penanda

    if angka < 2:
        is_prima = False
    else:
        for pembagi in range(2, angka):
            if angka % pembagi == 0:
                is_prima = False  # Ditemukan pembagi selain 1 dan dirinya
                break             # Hentikan pencarian

    return is_prima


# Studi Kasus: Uji Bilangan Prima
angka = int(input("Masukkan angka: "))

if cek_prima(angka):
    print(f"{angka} adalah BILANGAN PRIMA")
else:
    print(f"{angka} BUKAN bilangan prima")
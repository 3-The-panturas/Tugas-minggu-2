#==========================================#
#PRAKTIKUM 2: BILANGAN PRIMA & BREAK
#Simpan Sebagai: Praktikum_02.py
#==========================================#

# studi kasus: Uji Bilangan Prima
angka = int(input("Masukan Angka: "))
is_prima = True # flag penanda

if angka < 2:
    is_prima = False
else:
    for i in range(2, angka):
        if angka % i == 0:
            is_prima = False #Ditemukan pembagi selain 1 dan dirinya
            break # Hentikan pencarian

if is_prima: 
    print(f"{angka} adalah BILANGAN PRIMA")
else:
    print(f"{angka} BUKAN bilangan prima")
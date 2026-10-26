#===========================================
# Praktikum 03: DERET ARITMATIKA & AKUMULATOR
# Simpan sebagai : praktikum_03.py
#===========================================

print("======PROGRAM HITUNG DERET ARITMATIKA=========")

awal = int(input("Masukkan Suku Pertama (a): "))
beda = int(input("Masukkan Beda Deret (b): "))

banyak = int(input("Masukkan Banyak Suku (n): "))
while banyak <= 0:
    print("Peringatan: Banyak suku harus lebih dari 0!")
    banyak = int(input("Silahkan masukkan ulang banyak Suku(n): "))

suku = awal
total = 0

print("Barisan Deret: ", end="")
for i in range(banyak):
    print(suku, end=" ")
    total += suku
    suku += beda

print(f"Total Jumlah Seluruh Deret: {total}")
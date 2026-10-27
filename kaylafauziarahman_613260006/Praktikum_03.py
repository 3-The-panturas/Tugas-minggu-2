#==========================================#
#PRAKTIKUM 3: DERET ARITMATIKA & AKUMULATOR
#Simpan sebagai: praktikum_03.py
#==========================================#

print("=== PROGRAM HITUNG DERET ARITMATIKA ===")

awal = int(input("MASUKAN suku pertama (a): "))
beda = int(input("MASUKAN Beda Deret    (b):"))

# 1. IMPLEMENTASI WHILE: Validasi input jumlah suku agar harus positif (> 0)
banyak = int(input("Masukan Banyak Suku (n): "))
while banyak <= 0:
    print("peringatan: Banyak suka harus lebih dari 0!")
    banyak = int(input("Silahkan masukan ulang Banyak Suku (n): "))

# 2. IMPLETMENTASI FOR & AKUMULATOR: Mencetak deret dan menjumlah totalnya
suku = awal
total = 0 # Celengan Akumulator

print("Barisan Deret: ", end="")
for i in range(banyak):
    print(suku, end=" ")
    total += suku  # Akumulasi penjumlahan bertahap
    suku += beda   # Menyiapkan suku berikutnya

print(f"Total Jumlah Seluruh Deret = {total}")
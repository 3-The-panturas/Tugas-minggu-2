# =======================================
# PRAKTIKUM 3:DERET ARIMATIKA & AKUMULATOR
# Simpanan sebagai: praktikum_03.py
# =======================================

print("=== PROGRAM HITUNG DERET ARITMARIKA ===")

awal = int(input ("Masukkan Suku Pertama (a): "))
beda = int(input ("Masukkan Beda Deret (b): "))

# 1. IMPLEMENTASI WHILR: Validasi input julah suku agar harus positif (> 0)
banyak = int(input("Masukkan Banyak Suku (n): "))
while banyak <= 0:
    print("Peringatan Banyak suku harus lebih dari 0")
    banyak = int(input("Silahkan masukkan ulang Banyak suku (n): "))

# 2. IMPLEMENTASI FOR & AKUMULATOR: Mencetak deret dan menjumlahkan totslnya
suku = awal 
total = 0 # Celengan Akumulator

print("Barisan Deret: ", end="")
for i in range(banyak):
    print(suku, end=" ")
    total += suku # Akumulasi Penjumlahan Bertahap
    suku += beda # Menyiapkan suku berikutnya

print(f"Total Jumlah Seluruh deret = {total}")
 
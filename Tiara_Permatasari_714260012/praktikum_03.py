# =================================
# PRAKTIKUM 3: DERET ARITMATIKA & AKUMULATOR
# Simpan sebagai: praktikum_03.py
# ==================================

print("=== PROGRAM HITUNG DERET ARITMATIKA ===")

awal = int(input("Masukkan Suku Pertama (a): "))
beda = int(input("Masukkan Beda Deret       (b): "))

# 1. IMPLEMENTASI WHILE: Validasi input jumlah suku agar harus positif (> 0)
banyak = int(input("Masukkan Banyak Suku    (n): "))
while banyak <= 0:
    print("Peringatan: Banyak suku harus lebih dri 0!")
    banyak = int(input("Silahkan masukkan ulang Banyak Suku (n) "))

# 2. IMPLEMENTASI FOR & AKUMULATOR: Mencetak deret dan menjumlahkan totalnya
suku = awal
total = 0 # Celengan Akumulator

print("Barisan Deret: ", end="")
for i in range(banyak):
    print(suku, end=" ")
    total += suku       # Akumuklasi penjumlahan bertahap
    suku += beda        # Menyiapkan suku berikutnya

    print(f"Total Jumlah Seluruh Deret = {total}")
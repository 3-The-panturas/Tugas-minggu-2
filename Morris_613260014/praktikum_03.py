print("=== PROGRAM HITUNG DERET ARITMATIKA ===")

awal = int(input("Masukkan suku pertama (a): "))
beda = int(input("Masukkan beda deret (b): "))

# 1 IMPLEMENTASI WHILE: Validasi input jumlah suku agar harus positif (> 0)
banyak = int(input("Masukkan Banyak Suku  (n): "))
while banyak <= 0:
    print("Peringatan: Banyak Suku harus lebih dari 0!")
    banyak = int(input("Silakan masukkan ulang Banyak Suku (n): "))

# 2. IMPLEMENTASI FOR & AKUMULATOR: Mencetak deret dan menjumlahkan totalnya
suku = awal
total = 0 # Celengan Akumulator

print("" \
"Barisan Deret: ", end="")
for i in range(banyak):
    print(suku, end=" ")
    total += suku     # Akumulasi penjumlahan bertahap
    suku += beda      # Menyiapkan suku berikutnya

print(f"Total Jumlah Seluruh Deret = {total}")
#===========================================
# Praktikum 04: NESED LOOP & PENGOLAHAN LIST
# Simpan sebagai : praktikum_04.py
#===========================================

for basis in range(1, 4):
    for kolom in range(1, 4):
        print(f"{basis} x {kolom} = {basis * kolom}", end="\t")
    print()  # Pindah baris

nilai_maba = [12, 32, 35]
nilai_maba.append(95)

print("Daftar Nilai:", nilai_maba)
print("Nilai Tertinggi:", max(nilai_maba))
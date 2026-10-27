# ============================================
# PRAKTIKUM 4: NESTED LOOP & PENGOLAHAN LIST
# Simpanan sebagai: pratikum_04.py
# =============================================

for baris in range(1, 4):
    for kolom in range(1, 4):
        print(f"{baris}x{kolom}={baris*kolom}", end=" ")
    print() # pindah baris

# 2. pengenalan List Data Nilai
nilai_maba = [12, 32-35]
nilai_maba.append(95) # Menambah data di akhir 

print("Daftar nilai :", nilai_maba)
print("nilai tertinggi:", max(nilai_maba))

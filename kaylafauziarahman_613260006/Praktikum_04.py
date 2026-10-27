#==========================================#
# PRAKTIKUM 4: NESTED LOOP & PENGOLAHAN LIST
# Simpan Sebagai: praktikum_04.py
#==========================================#

for baris in range(1, 4):
    for kolom in range(1, 4):
        print(f"{baris}x{kolom})={baris*kolom}", end=" ")
    print() #pindah baris

# 2. Pengenalan List Data Niliai 
nilai_maba = [12, 32, 35]
nilai_maba.append(95)  #Menambah data di akhir

print("Daftar Nilai:", nilai_maba)
print("Nilai Tertinggi:", max(nilai_maba))
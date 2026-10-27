kehadiran = int(input("jumlah kehadiran (1-14): "))
nilai = int(input("Nilai ujian (0-100): "))
if kehadiran >= 12:
    if Nilai >= 75:
        print(":Lulus - Nilai Memuaskan")
    else:
        print("REMEDIAL - Nilai ujian kurang")
else:
    print("TIDAK LULUS - Kehadiran kurang dari 12")
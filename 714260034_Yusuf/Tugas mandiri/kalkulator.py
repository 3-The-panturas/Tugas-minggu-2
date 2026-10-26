#===========================================
# PROGRAM UTAMA: kalkulator.py
# Aplikasi Kalkulator konsol Bermenu Interaktif
#===========================================
import operasi3

while True:
    print("\n" + "=" * 45)
    print("     APLIKASI KALKULATOR KONSOL")
    print("=" * 45)
    print("1. Operasi Aritmatika Dasar (+, -, *, /)")
    print("2. Cek Sifat Bilangan (ganjil/genap)")
    print("3. Hitung Deret Aritmatika(For & Akumulator)")
    print("4. Cetak Tabel Perkalian Matriks(Nested Loop)")
    print("5. Keluar")
    print("=" * 45)

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "5":
        print("\n=== Terima kasih telah menggunakan kalkulator konsol. program selesai ===")
        break
    elif pilihan == "1":
        print("\n=== Operasi Aritmatika Dasar ===")
        print("A. Penjumlahan (+)")
        print("B. Pengurangan (-)")
        print("C. Perkalian (*)")
        print("D. Pembagian (/)")

        op = input("Pilih operasi (A/B/C/D): ").upper()

        if op in ["A", "B", "C", "D"]:
            inp1 = input("Masukkan angka pertama: ")
            inp2 = input("Masukkan angka kedua: ")

            if inp1.isdigit() and inp2.isdigit():
                a = float(inp1)
                b = float(inp2)

                if op == "A":
                    hasil = operasi3.tambah(a, b)
                    print(f"Hasil: {a} + {b} = {hasil:.2f}")
                elif op == "B":
                    hasil = operasi3.kurang(a, b)
                    print(f"Hasil: {a} - {b} = {hasil:.2f}")
                elif op == "C":
                    hasil = operasi3.kali(a, b)
                    print(f"Hasil: {a} * {b} = {hasil:.2f}")
                elif op == "D":
                    hasil = operasi3.bagi(a, b)
                    if isinstance(hasil, str):  # Jika hasil adalah pesan error
                        print(hasil)
                    else:
                        print(f"Hasil: {a} / {b} = {hasil:.2f}")
    elif pilihan == "2":
        print("\n=== Cek Sifat Bilangan (Ganjil/Genap) ===")
        inp_angka = input("Masukkan angka: ")

        if inp_angka.isdigit():
            angka = int(inp_angka)
            status = operasi3.cek_ganjil_genap(angka)
            print(f"Hasil: Angka {angka} tergolong bilangan {status}.")
        else:
            print("Peringatan: Masukkan harus berupa angka murni")

    elif pilihan == "3":
        print("\n=== Hitung Deret Aritmatika ===")
        inp_a = input("Masukkan Suku Pertama (a): ")
        inp_b = input("Masukkan Beda Deret (b): ")
        inp_n = input("Masukkan Banyak Suku (n): ")

        if inp_a.isdigit() and inp_b.isdigit() and inp_n.isdigit():
            a = int(inp_a)
            b = int(inp_b)
            n = int(inp_n)

            while n <= 0:
                print("Peringatan: Banyak suku harus lebih dari 0!")
            else:
                deret, total = operasi3.hitung_deret_aritmatika(a, b, n)
                print("Barisan Deret: ", " ".join(map(str, deret)))
                print(f"Total Jumlah Seluruh Deret: {total}")
    elif pilihan == "4":
        print("\n=== Cetak Tabel Perkalian Matriks ===")
        for baris in range(1, 4):
            for kolom in range(1, 4):
                print(f"{baris * kolom}\t", end=" ")
            print()  # Pindah ke baris berikutnya
    else:
        print("Pilihan tidak valid! Silakan pilih menu antara 1 hingga 5.")
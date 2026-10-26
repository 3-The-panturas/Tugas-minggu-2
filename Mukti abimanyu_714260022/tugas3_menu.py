import operasi13

while True:
    print("\n" + "=" * 45)
    print("=== APLIKASI KALKULATOR ===")
    print("=" * 45)
    print("1. Operasi aritmatika dasar (+, -, *, /)")
    print("2. Cek sifat bilangan ganjil/genap")
    print("3. Hitung derert aritmatika")
    print("4. Cetak tabel perkalian matriks")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "5":
        print("Terima kasih telah menggunakan kalkulator ini. Sampai jumpa!")
        break
    elif pilihan == "1":
        print("\n--- Sub menu operasi dasar ---")
        print("A. Penjumlahan (+)")
        print("B. Pengurangan (-)")
        print("C. Perkalian (*)")
        print("D. Pembagian (/)")

        op = input("Pilih operasi (A/B/C/D): ").upper()

        if op in ["A", "B", "C", "D"]:
            inp1 = input("Masukkan angka pertama: ")
            inp2 = input("Masukkan angka kedua: ")

            if inp1.isdigit() and inp2.isdigit():
                a = int(inp1)
                b = int(inp2)

                if op == "A":
                    hasil = operasi13.tambah(a, b)
                    print(f"Hasil {a} + {b} = {hasil}")
                elif op == "B":
                    hasil = operasi13.kurang(a, b)
                    print(f"Hasil {a} - {b} = {hasil}")
                elif op == "C":
                    hasil = operasi13.kali(a, b)
                    print(f"Hasil {a} * {b} = {hasil}")
                elif op == "D":
                    hasil = operasi13.bagi(a, b)
                    print(f"Hasil {a} / {b} = {hasil}")
            else:
                print("Peringatan: Masukan wajib berupa bilangan bulat!.")
        else:
            print("Peringatan: Pilihan operasi tidak valid!.")

    elif pilihan == "2":
        print("\n--- Cek Ganji/ Genap (Modulus %) ---")
        inp_angka = input("Masukkan angka bulat positif: ")

        if inp_angka.isdigit():
            angka = int(inp_angka)
            status = operasi13.cek_ganjil_genap(angka)
            print(f"{angka} tergolong bilangan {status}.")
        else:
            print("Peringatan: Masukan harus berupa angka murni!.")
        
    elif pilihan == "3":
        print("\n--- Hitung Deret Aritmatika ---")
        inp_a = input("suku pertama (a): ")
        inp_b = input("beda deret (b): ")
        inp_n = input("jumlah suku (n): ")

        if inp_a.isdigit() and inp_b.isdigit() and inp_n.isdigit():
            a = int(inp_a)
            b = int(inp_b)
            n = int(inp_n)

            while n <= 0:
                print("Peringatan: Jumlah suku (n) harus lebih dari 0!.")
                n = int(input("Masukkan ulang suku (n): "))

            total_deret = operasi13.hitung_deret_aritmatika(a, b, n)
            print(f"total jumlah deret = {total_deret}")
        else:
            print("Peringatan: seluruh masukan wajib berupa bilangan bulat!.")

    elif pilihan == "4":
        print("\n--- Matriks Tabel Perkalian 1-3 ---")
        for baris in range(1, 4):
            for kolom in range(1, 4):
                print(f"{baris * kolom}\t", end=" ")
            print()

else:
    print("Pilihan tidak valid! Silahkan masukkan opsi 1 sampai 5.")
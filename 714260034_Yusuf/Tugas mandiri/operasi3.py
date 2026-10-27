def tambah(a, b):
    """Mengembalikan hasil penjumlahan a + b."""
    return a + b
def kurang(a, b):
    """Mengembalikan hasil pengurangan a - b."""
    return a - b
def kali(a, b):
    """Mengembalikan hasil perkalian a * b."""
    return a * b
def bagi(a, b):
    """Mengembalikan hasil pembagian a / b. Jika b = 0, mengembalikan None."""
    if b == 0:
        return "Error: Pembagi tidak boleh nol."
    return a / b
def cek_ganjil_genap(angka):
    """Memeriksa sifat bilangan ganjil atau genap. Mengembalikan 'Ganjil' jika angka ganjil, 'Genap' jika angka genap."""
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

def hitung_deret_aritmatika(awal, beda, n):
    """Menghitung total akumulasi deret menggunakan perulangan for"""
    deret = []
    total = 0
    suku = awal
    for i in range(n):
        deret.append(suku)
        total += suku
        suku += beda
    return deret, total
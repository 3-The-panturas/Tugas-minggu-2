def tambah(a, b):
    """Mengembalikan hasil penjumlahan a + b"""
    return a + b

def kurang(a, b):
    """Mengembalikan hasil pengurangan a - b"""
    return a - b

def kali(a, b):
    """Mengembalikan hasil perkalian a * b"""
    return a * b

def bagi(a, b):
    """Mengembalikan hasil pembagian a / b."""
    if b == 0:
        return "Error: pembagian dengan nol"
    return a / b

def hitung_deret_aritmatika(awal, beda, n):
    """Menghitung total akumulasi deret aritmatika"""
    total = 0
    suku = awal
    for i in range(n):
        total += suku
        suku += beda
    return total
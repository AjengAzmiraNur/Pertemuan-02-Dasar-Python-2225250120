# Konstanta tahun sekarang
TAHUN_SEKARANG = 2026

# Meminta input dari pengguna
nama = input("Nama: ")
nim = input("NIM: ")
kelas = input("Kelas: ")
tahun_lahir = int(input("Tahun Lahir: "))

# Menghitung Perkiraan Umur 
umur = TAHUN_SEKARANG - tahun_lahir
# Menampilkan Biodata 
print()
print(f"Nama: {nama}")
print(f"NIM: {nim}")
print(f"kelas: {kelas}")
print(f"umur: sekitar {umur} tahun")

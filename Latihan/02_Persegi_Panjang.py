# Meminta input panjang dan lebar
panjang = float(input("Panjang: "))
lebar = float(input("Lebar: "))

# Menghitung luas dan keliling
luas = panjang * lebar
keliling = 2 * (panjang + lebar)

# Menampilkan hasil dengan 2 angka desimal
print(f"Luas      : {luas:.2f}")
print(f"Keliling  : {keliling:.2f}")
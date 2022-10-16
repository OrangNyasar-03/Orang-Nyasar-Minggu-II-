print("Menghitung Luas Dan Volume Dari Balok")
print("Masukkan Nilai Dari Panjang")
p = int(input())
print("Masukkan Nilai Dari Lebar")
l = int(input())
print("Masukkan Nilai Dari Tinggi")
t = int(input())
luas = 2 * p * l + 2 * p * t + 2 * l * t
volume = p * l * t
print("Luas Dari Balok Adalah: " + str(luas))
print("Volume Dari Balok Adalah: " + str(volume))

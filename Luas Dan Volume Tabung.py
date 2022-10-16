print("Masukkan Nilai Dari Jari-Jari")
r = int(input())
print("Masukkan Nilai Dari Tinggi")
t = int(input())
luasSelimut = 2 * (float(22) / 7) * r * t
luasPermukaan = 2 * (float(22) / 7) * r * (r + t)
volume = float(22) / 7 * (r * r) * t
print("Luas Selimut Dari Tabung Adalah: " + str(luasSelimut))
print("Jumlah Luas Permukaan Dari Tabung Adalah: " + str(luasPermukaan))
print("Jumlah Volume Dari Tabung Adalah: " + str(volume))

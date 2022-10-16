print("Masukkan Nilai Dari Jari-Jari")
r = int(input())
print("Masukkan Nilai Dari Sisinya")
s = int(input())
print("Masukkan Nilai Tingginya")
t = int(input())
luasSelimut = float(22) / 7 * r * s
luasPermukaan = 3.14 * r * s + 3.14 * (r * 2)
volume = float(1) / 3 * 3.14 * r * r * t
print("Jumlah Luas Selimut Pada Kerucut Adalah: " + str(luasSelimut))
print("Jumlah Luas Permukaan Pada Kerucut Adalah: " + str(luasPermukaan))
print("Jumlah Volume Pada Kerucut Adalah: " + str(volume))

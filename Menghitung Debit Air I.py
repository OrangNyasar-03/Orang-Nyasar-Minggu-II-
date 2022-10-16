print("Masukan Volume Air")
volume = int(input())
volume = volume * 1000
print("Masukkan Lama Waktu Pengisian")
waktu = int(input())
waktu = waktu * 60
debit = float(volume) / waktu
print("Debit Air Adalah: " + str(debit) + "m3/Detik")

print("Masukkan Volume Air")
volume = int(input())
volume = volume * 1000
print("Masukkan Waktu Air")
waktu = int(input())
waktu = waktu * 3600
debit = float(volume) / waktu
print("Debit Air Yang Keluar Adalah: " + str(debit) + "Liter/detik")

print("Masukka Debit Air")
debit = int(input())
print("Masukkan Jumlah Lama Waktu")
waktu = int(input())
waktu = waktu * 60
volume = debit * waktu
print("Banyak Air Yang Bisa Dipindahkan Adalah: " + str(volume) + " Liter ")

print("Masukkan Jarak Pada Peta")
jarakPadaPeta = float(input())
print("Masukkan Jarak Sesungguhnya")
jarakSesungguhnya = float(input())
jarakSesungguhnya = jarakSesungguhnya * 100000
print("Jarak sesungguhnya di konfersikan ke cm" + str(jarakSesungguhnya))
skala = jarakSesungguhnya / 10
print("jumlah skala " + str(skala) + ", karena memiliki Nol setelah angka pertama maka, nol si setiap bagian di hapus maka akan menjadi: " + "1:" + str(skala))

age = 19

message1 = "umur kamu " + str(age)# line ini tidak menggunakan formatted string karena kita harus mengubah integer menjadi string
message2= f"umur kamu {age}"# line ini menggunakan formatted string karena kita cukup memasukkan fungsi dari formatted string maka integer akan otomatis di ubah menjadi string
print(message1)
print(message2)
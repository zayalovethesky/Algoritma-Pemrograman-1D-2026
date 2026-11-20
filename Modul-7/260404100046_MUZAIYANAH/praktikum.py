##CARA BUAT DICTIONARY PY
# dict = {'Name': 'Zara', 'Age':7, 'Class':'First'}
# print("dict['Name']:", dict['Name'])
# print("dict['Age']:", dict['Age'])



##DICTIONARY PYTHON
# dict = {'Name':'Zara','Age':7, 'Class':'First'}
# dict['Age'] = 8
# dict['School'] = "DPS School"

# print("dict['Age']:", dict['Age'])
# print("dict['School']:", dict['School'])



# CARA MENGHAPUS PADA DICTIONARY PY
# dict = {'Name':'Zara','Age':7, 'Class': 'First'}
# del dict['Name']
# dict.clear()
# del dict
# print("dict['Age']:", dict['Age'])
# print("dict['School']:", dict['School'])



# angka = int("abc")
# print("Program selesai")

# try:
#     angka = int("abc")
#     print(angka)
# except ValueError:
#     print("Input harus berupa angka")
    
# print("Program Selesai")





# mahasiswa = {"Andi":85, "Budi":90}
# try:
#     print(mahasiswa["Citra"])
# except KeyError:
#     print("Nama tidak ditemukan")





# hobi = {"membaca", "menulis"}

# try:
#     hobi.remove("berenang")
# except KeyError:
#     print("Elemen tidak ada di himpunan")





# kosong = set()

# try:
#     kosong.pop()

# except KeyError as e:
#     print("Error:", e)


# Dictionary#
# nilai = {
#     "SEAN"   : 90,
#     "KEONHO" : 89,
#     "JAMES"  : 85,
#     "Martin" : 92,
#     "JUHOON" : 88,
# }

# print("The name w highes score is", max(nilai,key=nilai.get))
# print("The average is", sum(nilai.values())/len(nilai))

# python     = {"Sean", "Kono", "Juhoon"}
# javaScript = {"James", "Martin", "Juhoon"}

# print("\nGabungan :", python | javaScript)
# print("Ikut keduanya :", python & javaScript)
# print("Ikut salah satunya :", python - javaScript)
# print("Ikut salah satunya ", javaScript - python)
# print("Adalah pokonya :", python ^ javaScript)


# contoh ={'nama': 'zay', 'umur':'17'}

# nama= {1, 2, 3, 4, 4}
# nama2 = {4, 5, 6, 7, 8}

# print(nama | nama2)
# print(nama & nama2)
# print(nama - nama2)
# print(nama ^ nama2)


# x = {1, 2, 3, 4, 4}
# y = {1, 3, 4, 5, 6, 7, 8}

# z = y.symmetric_difference(x)

# print(z)


# x = {2, 3, 4}

# try:
#     x.pop()
# except KeyError as e:
#     print("Error :", e)





# kosong = {}

# try:
#     kosong.pop()
#     print("try berhasil")
# except TypeError:
#     print("try gagal")
    

# try:  
#     print(10/0)
# except ZeroDivisionError:
#     print("AP CBA CBA")
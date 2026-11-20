tugas = {}

while True:
    print("\nTO DO LIST")
    print("1. Tambah tugas")
    print("2. Tampilkan semua tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Lihat semua tugas yang selesai dan belum")
    print("6. Keluar")   
    pilihan = input("\nPilih menu(1-6) :").strip()
    
    if pilihan == "1":
        namaTugas = input("Masukkan nama tugas :").strip().lower()
        if namaTugas in tugas:
            print("Tugas", namaTugas, "sudah ada.")
        else:
            tugas[namaTugas] = "Belum selesai"
            print("Tugas", namaTugas, "berhasil ditambahkan!")
            
    elif pilihan == "2":
        if len(tugas) == 0:
            print("Masih belum ada tugas")
        else:
            print("\nDaftar tugas")
            nomor = 1
            for namaTugas in tugas:
                print(str(nomor) + "." + namaTugas + "—" + tugas[namaTugas])
                nomor +=1
        
    elif pilihan == "3":
        namaTugas = input("Masukkan nama tugas yang selesai :").strip().lower()
        if namaTugas in  tugas:
            tugas[namaTugas] = "Telah selesai!"
            print("Tugas", namaTugas, "ditandai selesai")
        else:
            print("Tugas", namaTugas, "tidak ditemukan")
            
    elif pilihan == "4":
        namaTugas = input("Masukkan nama tugas yang ingin di hapus :").strip().lower()
        try:
            del tugas[namaTugas]
            print("Tugas", namaTugas, "telah berhasil dihapus!")
        except KeyError:
            print("Tugas", namaTugas, "tidak ditemukan!")
            
    elif pilihan == "5":
        daftarSelesai = []
        daftarBelum = []
        for namaTugas in tugas:
            if tugas[namaTugas] == "Telah selesai!":
                daftarSelesai.append(namaTugas)
            else:
                daftarBelum.append(namaTugas)
                
        print("\nTugas selesai :", len(daftarSelesai))
        if len(daftarSelesai) == 0:
            print("- (tidak ada)")
        else:
            for namaTugas in daftarSelesai:
                print("-", namaTugas)
        print("Tugas belum selesai :", len(daftarBelum)) 
        if len(daftarBelum) == 0:
            print("- (tidak ada)")
        else:
            for namaTugas in daftarBelum:
                print("-", namaTugas)
                
    elif pilihan == "6":
        print("Program selesai!")
        break
    else:
        print("Pilihan tidak valid, silahkan pilih kembali(1-6)!")          
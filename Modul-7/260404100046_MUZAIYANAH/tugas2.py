playlist = {}

while True:
    print("\nPENGELOLA PLAYLIST MUSIK")
    print("1. Buat playlist")
    print("2. Tambah lagu ke playlist")
    print("3. Tampilkan semua playlist dan lagunya")
    print("4. Cari lagu")
    print("5. Hapus lagu dari playlist")
    print("6. Hapus playlist")
    print("7. Keluar")
    pilihan = input("\nPilih menu(1-7) :").strip()

    if pilihan == "1":
        namaPlaylist = input("Masukkan nama playlist :").strip().lower()
        if namaPlaylist in playlist:
            print("Playlist", namaPlaylist, "sudah ada.")
        else:
            playlist[namaPlaylist] = {}
            print("Playlist", namaPlaylist, "berhasil dibuat!")

    elif pilihan == "2":
        namaPlaylist = input("Masukkan nama playlist :").strip().lower()
        try:
            lagu = playlist[namaPlaylist]
            judul = input("Masukkan judul lagu :").strip().lower()
            penyanyi = input("Masukkan nama penyanyi :").strip()
            if judul in lagu:
                print("Lagu", judul, "sudah ada di playlist", namaPlaylist)
            else:
                lagu[judul] = penyanyi
                print("Lagu", judul, "berhasil ditambahkan ke playlist", namaPlaylist)
        except KeyError:
            print("Playlist", namaPlaylist, "tidak ditemukan!")

    elif pilihan == "3":
        if len(playlist) == 0:
            print("Masih belum ada playlist")
        else:
            for namaPlaylist in playlist:
                print("\nPlaylist:", namaPlaylist)
                if len(playlist[namaPlaylist]) == 0:
                    print("  (belum ada lagu)")
                else:
                    nomor = 1
                    for judul in playlist[namaPlaylist]:
                        print("  " + str(nomor) + ". " + judul + " - " + playlist[namaPlaylist][judul])
                        nomor += 1

    elif pilihan == "4":
        judul = input("Masukkan judul lagu yang dicari :").strip().lower()
        ditemukan = False
        for namaPlaylist in playlist:
            try:
                penyanyi = playlist[namaPlaylist][judul]
                print("Lagu", judul, "oleh", penyanyi, "ada di playlist", namaPlaylist)
                ditemukan = True
            except KeyError:
                pass
        if not ditemukan:
            print("Lagu", judul, "tidak ditemukan!")

    elif pilihan == "5":
        namaPlaylist = input("Masukkan nama playlist :").strip().lower()
        judul = input("Masukkan judul lagu yang ingin dihapus :").strip().lower()
        try:
            lagu = playlist[namaPlaylist]
            try:
                del lagu[judul]
                print("Lagu", judul, "berhasil dihapus dari playlist", namaPlaylist)
            except KeyError:
                print("Lagu", judul, "tidak ditemukan di playlist", namaPlaylist)
        except KeyError:
            print("Playlist", namaPlaylist, "tidak ditemukan!")

    elif pilihan == "6":
        namaPlaylist = input("Masukkan nama playlist yang ingin dihapus :").strip().lower()
        try:
            del playlist[namaPlaylist]
            print("Playlist", namaPlaylist, "berhasil dihapus!")
        except KeyError:
            print("Playlist", namaPlaylist, "tidak ditemukan!")

    elif pilihan == "7":
        print("Program selesai!")
        break

    else:
        print("Pilihan tidak valid, silahkan pilih kembali(1-7)!")
undangan = set()
webinarA = set()
webinarB = set()

print("DAFTAR UNDANGAN")
data = (input("Masukkan nama undangan : "))
undangan = set(data.split(", "))

print("\nPESERTA WEBINAR A")
data = (input("Masukkan nama peserta Webinar A : "))
webinarA = set(data.split(", "))

print("\nPESERTA WEBINAR B")
data = (input("Masukkan nama peserta Webinar B : "))
webinarB = set(data.split(", "))

semuaPeserta = webinarA | webinarB
hadirKeduanya = webinarA & webinarB
hanyaSalahSatu = webinarA ^ webinarB
tidakHadir = undangan - (webinarA|webinarB)

print("\nHASIL:")
print("Semua peserta dari kedua webinar :", semuaPeserta)
print("Peserta yang hadir di keduanya   :", hadirKeduanya)
print("Peserta yang hanya hadir di satu :", hanyaSalahSatu)
print("Undangan yang tidak hadir        :", tidakHadir)







# undangan = set()
# webinarA = set()
# webinarB = set()

# print("DAFTAR UNDANGAN")
# while True:
#     nama = input("Masukkan nama undangan (ketik 'selesai' untuk berhenti): ").strip().lower()
#     if nama == "selesai":
#         break
#     undangan.add(nama)

# print("\nPESERTA WEBINAR A")
# while True:
#     nama = input("Masukkan nama peserta Webinar A (ketik 'selesai' untuk berhenti): ").strip().lower()
#     if nama == "selesai":
#         break
#     webinarA.add(nama)

# print("\nPESERTA WEBINAR B")
# while True:
#     nama = input("Masukkan nama peserta Webinar B (ketik 'selesai' untuk berhenti): ").strip().lower()
#     if nama == "selesai":
#         break
#     webinarB.add(nama)

# semuaPeserta = webinarA | webinarB
# hadirKeduanya = webinarA & webinarB
# hanyaSalahSatu = webinarA ^ webinarB
# tidakHadir = undangan - semuaPeserta

# print("\nHASIL:")
# print("Semua peserta dari kedua webinar :", ", ".join(sorted(semuaPeserta)))
# print("Peserta yang hadir di keduanya   :", ", ".join(sorted(hadirKeduanya)))
# print("Peserta yang hanya hadir di satu :", ", ".join(sorted(hanyaSalahSatu)))
# print("Undangan yang tidak hadir        :", ", ".join(sorted(tidakHadir)))





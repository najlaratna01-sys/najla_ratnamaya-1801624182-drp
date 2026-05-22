print("=== Daftar Aktivitas Harian ===")

# list kosong
daftar_aktivitas = []

# jumlah aktivitas
jumlah = int(input("Berapa aktivitas yang ingin ditambahkan? "))

# perulangan input
for i in range(jumlah):

    print(f"\nAktivitas ke-{i+1}")

    aktivitas = input("Masukkan aktivitas: ")
    waktu = input("Masukkan waktu aktivitas: ")
    kategori = input("Masukkan kategori aktivitas: ")
    status = input("Status (selesai/belum): ")

    # gabungkan data
    data = f"""
Aktivitas : {aktivitas}
Waktu     : {waktu}
Kategori  : {kategori}
Status    : {status}
"""

    # masukkan ke list
    daftar_aktivitas.append(data)

# tampilkan hasil
print("\n=== DAFTAR AKTIVITAS ===")

for item in daftar_aktivitas:
    print(item)

print("Terima kasih telah menggunakan program!")

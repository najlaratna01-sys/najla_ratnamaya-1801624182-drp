from datetime import datetime

print("=== Aplikasi Manajemen Aktivitas ===")

aktivitas = input("Masukkan aktivitas: ")

# =========================
# AKTIVITAS SARAPAN
# =========================
if aktivitas == "sarapan":

    menu = input("Masukkan menu sarapan: ")

    if menu == "telur":
        print("Bahan tersedia")
        print("Silakan masak telur terlebih dahulu")

    elif menu == "ikan":
        print("Bahan tersedia")
        print("Silakan masak ikan terlebih dahulu")

    elif menu == "nugget":
        print("Bahan tersedia")
        print("Silakan masak nugget terlebih dahulu")

    else:
        print("Bahan tidak tersedia")
        print("Silakan beli bahan terlebih dahulu")

# =========================
# AKTIVITAS BERANGKAT KERJA
# =========================
elif aktivitas == "berangkat kerja":

    # mengambil waktu sekarang dari komputer
    sekarang = datetime.now()

    # menentukan jam masuk kerja
    jam_masuk = sekarang.replace(hour=8, minute=0, second=0)

    # menampilkan waktu sekarang
    print("Waktu sekarang:", sekarang.strftime("%H:%M:%S"))

    # cek apakah terlambat
    if sekarang > jam_masuk:
        print("Anda sudah terlambat masuk kerja!")

    else:
        print("Anda belum terlambat")
        print("Hati-hati di jalan!")

# =========================
# JIKA INPUT SALAH
# =========================
else:
    print("Aktivitas tidak dikenali")

    print("Terima kasih telah menggunakan aplikasi!")
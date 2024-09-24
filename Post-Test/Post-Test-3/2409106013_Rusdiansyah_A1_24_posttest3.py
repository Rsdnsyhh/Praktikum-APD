print("SELAMAT DATANG  DIKALKULATOR KEBUTUHAN KALORI HARIAN")
JenisKelamin = int(input("Masukkann jenis kelamin (pilihan 1 Pria) dan (pilihan 2 Wanita) = "))
Berat_Badan = float(input("Masukkan berat badan (dalam gram) = "))
Tinggi_Badan = float(input("Masukkan tinggi badan(dalam KM) = "))
Umur = int(input("Masukkan umur = "))

print("""
                level aktivitas harian
    1 Untuk aktivitas manual (jarang bergerak)
    2 Untuk aktivitas sedang (olahraga 1-3 kali seminggu)
    3 Untuk aktivitas tinggi (olahraga 4-7 kali seminggu)
""")
aktivitas = int(input("Pilih level aktivitas harian kalian = "))
if aktivitas == 1:
    Level_Aktivitas_Harian = 1.25
elif aktivitas == 2:
    Level_Aktivitas_Harian = 1.36
elif aktivitas == 3:
    Level_Aktivitas_Harian = 1.72
else:
    print("Pilihan tidak valid")
    exit()

Berat_Badan_Konversi = Berat_Badan / 1000
Tinggi_Badan_Konversi = Tinggi_Badan * 100000
BMR_Pria = (10 * Berat_Badan_Konversi) + (6.25 * Tinggi_Badan_Konversi) - (5 * Umur) + 5
BMR_Wanita = (10 * Berat_Badan_Konversi) + (6.25 * Tinggi_Badan_Konversi) - (5 * Umur) - 161

print("""
    Pilih rumus BMR yang anda ingin gunakan
            1 Untuk rumus BMR pria
            2 Untuk rumus BMR wanita
""")
Pilihan = int(input("Masukkan pilihan anda (1/2) = "))
if Pilihan == 1:
    KKKH = (BMR_Pria * Level_Aktivitas_Harian)
    print(f"{KKKH}")
elif Pilihan == 2:
    KKKH2 = (BMR_Wanita * Level_Aktivitas_Harian)
    print(f"{KKKH2}")
else:
    print("Pilihan tidak valid")
    exit(Pilihan)
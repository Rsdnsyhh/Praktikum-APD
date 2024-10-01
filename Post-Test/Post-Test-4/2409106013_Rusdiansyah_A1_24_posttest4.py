User_name = "Rusdy"
Pass_word = "13"

print("""
    <<------Silahkan Login Terlebih Dahulu------>>
    """)


Percobaan = 0

while Percobaan < 3:
    Username = input("Username : ")
    Password = input("Masukkan 3 digit angka NIM terakhir (tanpa angka 0) : ")
    if Username == User_name and Password == Pass_word:
        print("Anda Berhasil Login")
        break 
    else:
        print("Password atau Username yang anda masukkan salah")
        Percobaan += 1


if Percobaan < 3:
    while True:
        print("""
        <<------SELAMAT DATANG  DIKALKULATOR KEBUTUHAN KALORI HARIAN------>>
        """)
        Jenis_Kelamin = int(input("Masukkann jenis kelamin (pilihan 1 Pria) dan (pilihan 2 Wanita) = "))
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

        Berat_Badan_Konversi = Berat_Badan / 1000
        Tinggi_Badan_Konversi = Tinggi_Badan * 100000
        BMR_Pria = (10 * Berat_Badan_Konversi) + (6.25 * Tinggi_Badan_Konversi) - (5 * Umur) + 5
        BMR_Wanita = (10 * Berat_Badan_Konversi) + (6.25 * Tinggi_Badan_Konversi) - (5 * Umur) - 161

        if Jenis_Kelamin == 1:
            KKKH = (BMR_Pria * Level_Aktivitas_Harian)
            print(f"{KKKH}")
        elif Jenis_Kelamin == 2:
            KKKH2 = (BMR_Wanita * Level_Aktivitas_Harian)
            print(f"{KKKH2}")
        else:
            print("Pilihan tidak valid")

        menu = int(input("Masukkan (1) mengulang program , jika pilihan (2) program diberhentikan : "))
        if menu == 1:
            pass
        elif menu == 2:
            break
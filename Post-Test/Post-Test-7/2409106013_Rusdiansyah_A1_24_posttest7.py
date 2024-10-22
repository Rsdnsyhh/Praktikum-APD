Data_Rekening_Nasabah = {}

def Tampilkan_Menu_Pilihan():
    print("""
<=======================================================>
    |   SELAMAT DATANG DI PROGRAM BANK SEDERHANA   |
<=======================================================>
    |                1. Buat Rekening              |
    |                2. Cek Saldo                  |           
    |                3. Isi Saldo                  |          
    |                4. Tarik Saldo                |     
    |                5. Hapus Akun                 |      
    |                0. Exit                       |  
<=======================================================>
""")

def Masukkan_Nomor_Rekening():
    return input("Masukkan Nomor Rekening: ")

def Buat_Rekening(Nasabah, Nomor_Rekening):
    if Nomor_Rekening in Data_Rekening_Nasabah:
        print("Yeyy,Nomor Rekening Anda Telah Terdaftar.")
    else:
        Data_Rekening_Nasabah[Nomor_Rekening] = {"Nama": Nasabah, "Saldo": 0}
        print("Rekening berhasil dibuat.")

def Cek_Saldo(Nomor_Rekening):
    if Nomor_Rekening in Data_Rekening_Nasabah:
        Nasabah = Data_Rekening_Nasabah[Nomor_Rekening]
        print(f"NAMA NASABAH: {Nasabah['Nama']}\nSALDO: {Nasabah['Saldo']}")
    else:
        print("Nomor Rekening tidak ditemukan.")

def Isi_Saldo(Nomor_Rekening, Nominal):
    if Nominal <= 0:
        print("Nominal harus lebih besar dari 0.")
        return
    if Nomor_Rekening in Data_Rekening_Nasabah:
        Data_Rekening_Nasabah[Nomor_Rekening]['Saldo'] += Nominal
        print("TopUp saldo berhasil.")
    else:
        print("Nomor Rekening tidak ditemukan.")
        Kembali_Lagi = input("Mau coba lagi? (ya/tidak): ")
        if Kembali_Lagi.lower() == 'ya':
            Nominal = float(input("Masukkan Nominal Setoran: "))
            Isi_Saldo(Nomor_Rekening, Nominal)

def Tarik_Saldo(Nomor_Rekening, Tarik_Nominal):
    if Nomor_Rekening in Data_Rekening_Nasabah:
        Saldo = Data_Rekening_Nasabah[Nomor_Rekening]['Saldo']
        if Tarik_Nominal  <= Saldo:
            Data_Rekening_Nasabah[Nomor_Rekening]['Saldo'] -= Tarik_Nominal
            print("Penarikan saldo berhasil.")
        else:
            print("Saldo tidak cukup.")
    else:
        print("Nomor Rekening tidak ditemukan.")

def Hapus_Akun():
    Nomor_Rekening = Masukkan_Nomor_Rekening()
    if Nomor_Rekening in Data_Rekening_Nasabah:
        del Data_Rekening_Nasabah[Nomor_Rekening]
        print("Akun berhasil dihapus.")
    else:
        print("Nomor Rekening tidak ditemukan.")

def Keluar_Program():
    Jawab = input("Apakah anda ingin keluar dari program? (ya/tidak): ")
    return Jawab.lower() == 'ya'

def Lanjutkan_Program():
    Jawab = input("Apakah anda ingin melakukan operasi program lainnya?? (ya/tidak): ")
    return Jawab.lower() == 'ya'

while True:
    Tampilkan_Menu_Pilihan()
    try:
        pilih = int(input("PILIH : "))
        
        if pilih == 1:
            Nama_Nasabah = input("Nama Nasabah: ")
            Nomor_Rekening = input("Nomor Rekening: ")
            Buat_Rekening(Nama_Nasabah, Nomor_Rekening)

        elif pilih == 2:
            Nomor_Rekening = Masukkan_Nomor_Rekening()
            Cek_Saldo(Nomor_Rekening)

        elif pilih == 3:
            Nomor_Rekening = Masukkan_Nomor_Rekening()
            Total = float(input("Masukkan Nominal Setoran: "))
            Isi_Saldo(Nomor_Rekening, Total)

        elif pilih == 4:
            Nomor_Rekening = Masukkan_Nomor_Rekening()
            Tarik_Saldo1 = float(input("Masukkan Nominal yang Ingin Ditarik: "))
            Tarik_Saldo(Nomor_Rekening, Tarik_Saldo1)

        elif pilih == 5:
            Hapus_Akun()

        elif pilih == 0:
            if Keluar_Program():
                print("Terima kasih telah menggunakan Program Bank Sederhana.")
                break

        else:
            print("Pilihan tidak valid. Silakan coba lagi yaa.")
        
        if not Lanjutkan_Program():
            print("Terima kasih telah menggunakan Program Bank Sederhana.")
            break

    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang benar yaa.")
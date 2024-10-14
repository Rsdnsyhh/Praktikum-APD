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

Data_Rekening_Nasabah = {}

while True:
    pilih = int(input("PILIH : "))
    
    if pilih == 1:
        Nama_Nasabah = input("NAMA NASABAH : ")
        Nomor_Rekening = input("NOMOR REKENING : ")
        Saldo = 0

        Data_Rekening_Nasabah[Nomor_Rekening] = {"Nama": Nama_Nasabah, "Saldo": Saldo}
        print("Anda Telah Berhasil Membuat Rekening")
    
    elif pilih == 2:
        Nomor_Rekening = input("Masukkan Nomor Rekening: ")
        if Nomor_Rekening in Data_Rekening_Nasabah:
            nasabah = Data_Rekening_Nasabah[Nomor_Rekening]
            print(f"\nREKENING ANDA\nNAMA NASABAH : {nasabah['Nama']}\nNOMOR REKENING : {Nomor_Rekening}\nSALDO : {nasabah['Saldo']}")
        else:
            print("Nomor Rekening tidak ditemukan.")
    
    elif pilih == 3:
        Nomor_Rekening = input("Masukkan Nomor Rekening: ")
        if Nomor_Rekening in Data_Rekening_Nasabah:
            Total = int(input("Masukkan Nominal Setoran : "))
            Data_Rekening_Nasabah[Nomor_Rekening]['Saldo'] += Total
            print("TopUp Saldo Berhasil")
        else:
            print("Nomor Rekening tidak ditemukan.")
    
    elif pilih == 4:
        Nomor_Rekening = input("Masukkan Nomor Rekening: ")
        if Nomor_Rekening in Data_Rekening_Nasabah:
            Tarik_Saldo = float(input("Masukkan Nominal Yang Ingin Anda Tarik : "))
            if Tarik_Saldo > Data_Rekening_Nasabah[Nomor_Rekening]['Saldo']:
                print("Saldo Anda Tidak Cukup")
            else:
                Data_Rekening_Nasabah[Nomor_Rekening]['Saldo'] -= Tarik_Saldo
                print("Penarikan Berhasil!")
        else:
            print("Nomor Rekening tidak ditemukan.")
    
    elif pilih == 5:
        Nomor_Rekening = input("Masukkan Nomor Rekening Anda Untuk Menghapus Akun : ")
        if Nomor_Rekening in Data_Rekening_Nasabah:
            del Data_Rekening_Nasabah[Nomor_Rekening]
            print("Akun Anda berhasil dihapus!!")
        else:
            print("Nomor Rekening tidak ditemukan.")
    
    elif pilih == 0:
        print("TERIMAKASIH TELAH MENGGUNAKAN PROGRAM BANK SEDERHANA INI.")
        break
    else:
        print("Pilihan tidak valid, silakan coba lagi.")
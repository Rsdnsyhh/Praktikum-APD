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

Data_Rekening_Nasabah = []
while True:
    pilih = int(input("PILIH : "))
    if pilih == 1:
        Nama_Nasabah = input("NAMA NASABAH : ")
        Nomor_Rekening = input("NOMOR REKENING : ")
        Saldo = 0
        Data_Rekening_Nasabah.append([Nama_Nasabah, Nomor_Rekening])
        print("Anda Telah Berhasil Membuat Rekening")
    elif pilih == 2:
        
        for i in range(len(Data_Rekening_Nasabah)):
            print(f"\n REKENING ANDA \nNAMA NASABAH : {Nama_Nasabah}\nNOMOR REKENING : {Nomor_Rekening}\nSALDO : {Saldo}")
    elif pilih == 3:
        Total = int(input("Masukkan Nominal Setoran  : "))
        Saldo += Total
        print("TopUp Saldo Berhasil")
    elif pilih == 4:
        Tarik_Saldo = float(input("Masukkan Nominal Yang Ingin Anda Tarik : "))
        if Tarik_Saldo > Total:
            print("Saldo Anda Tidak Cukup")
        else:
            Saldo -= Tarik_Saldo
            print("Penarikan Berhasil!")
    elif pilih == 5:
        Nomor_Rekening = input("Masukkan Nomor Rekening Anda Untuk Menghapus Akun : ")
        for i in range(len(Data_Rekening_Nasabah)):
            del Data_Rekening_Nasabah
            print("Akun Anda berhasil dihapus!!")
    elif pilih == 0:
        print("TERIMAKASIH TELAH MENGGUNAKAN PROGRAM BANK SEDERHANA INI.")
        break
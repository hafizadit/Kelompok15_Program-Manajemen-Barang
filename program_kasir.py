import datetime
import sys
import json

# Open and loads Json File
listbarang_json = open("Data/listbarang.json","r")
jsondata = listbarang_json.read()
listbarang_py = json.loads(jsondata)

password_json = open("Data/password.json","r")
jsondata2 = password_json.read()
password_py = json.loads(jsondata2)

# define list untuk program hitung
Id = []
harga_total = []
barang_total = []
jumlah_barang = []
list_belanja = [barang_total,jumlah_barang]

# Open file txt tempat mencatat transaksi yang terjadi
transaksi_txt = open("Data/transaksi.txt","a")
data_pembeli_txt = open("Data/data_pembeli.txt","a")

# Fungsi untuk menampilkan data barang
def display():
    print("")
    x = "List Barang"
    print(x.center(50))
    print("-"*50)
    print("ID   Nama Barang   Harga   Stok")
    print("-"*50)
    # Looping untuk print stok barang
    i = 0
    n = len(listbarang_py["list"])
    while i < n:
        print(f"({listbarang_py['list'][i]['ID']})   ({listbarang_py['list'][i]['Nama']})   ({listbarang_py['list'][i]['Harga']})   ({listbarang_py['list'][i]['Stok']})")
        i += 1
    print("")

# Fungsi pembayaran dan menampilkan struk
def struk():
    # Memilih Metode
    print("""\nMetode Pembayaran
1. Cash
2. Kredit DP 0%
*Terdapat pajak 2,5%
Pilih (1/2)
""",end="\n")
    metode = input(">> ")
    
    # Menampilkan List Belanja
    print("")
    print(list_belanja)
    bAdmin = 2500
    pajak = 0.025 * sum(harga_total)
    harga = bAdmin + pajak + sum(harga_total)
    print("\nTotal Harga Barang Belanjaan anda adalah (Belum Bunga):",harga)

    if int(metode) == 1:
        keterangan = "Cash"
        bayar = int(input("\nMasukkan Jumlah Uang :"))
        dp = 0
        sisa = 0
    elif int(metode) == 2:
        # Antisipasi input bukan angka
        try:
            angsuran = input("Masukkan berapa bulan angsuran\n6 (bunga 4%)\n12 (bunga 6%)\n24 (bunga 10%)\n>> ")
            angsuran = int(angsuran)
        except ValueError:
            print("\nError!\nInput Bukan Angka")
            print("")
            print("="*50)
            txt = "Program Selesai"
            print(txt.center(50))
            print("="*50)
            sys.exit()

        if angsuran == 6:
            bunga = 0.04
        elif angsuran == 12:
            bunga = 0.06
        elif angsuran == 24:
            bunga = 0.1
        else: # Jika input angsuran tidak tersedia
            print("\nError!\nJumlah Angsuran Tidak Terdaftar")
            print("")
            print("="*50)
            txt = "Program Selesai"
            print(txt.center(50))
            print("="*50)
            sys.exit()

        # Antisipasi input DP bukan angka
        try:
            dp = int(input("\nMasukkan jumlah DP :"))
        except ValueError:
            print("\nError!\nInput Bukan Angka")
            print("")
            print("="*50)
            txt = "Program Selesai"
            print(txt.center(50))
            print("="*50)
            sys.exit()

        bayar = dp
        harga = harga + (harga * bunga)
        sisa = harga - dp
        cicilan = sisa/angsuran
        keterangan = f"Kredit Angsuran\n{angsuran} bulan\nCicilan bunga {bunga*100} %\n{round(cicilan,2)} ({angsuran}x)"
    else:
        print("\nInput anda salah!\n")
        inp = input("Tekan enter untuk ulangi: ")
        if inp == "":
            struk()
            sys.exit()
        else:
            print("\nError!")
            print("")
            print("="*50)
            txt = "Program Selesai"
            print(txt.center(50))
            print("="*50)
            sys.exit()

    # Input Data Pembeli
    try:
        nama_pembeli = input("\nMasukkan nama pembeli : ")
        umur_pembeli = int(input("Masukkan umur pembeli : "))
        sex_pembeli = input("Masukkan gender pembeli : ")
        alamat_pembeli = input("Masukkan alamat pembeli : ")
    except ValueError:
        print("\nError! Input Umur Salah")
        print("")
        print("="*50)
        txt = "Program Selesai"
        print(txt.center(50))
        print("="*50)
        sys.exit()
    
    # Mendeteksi adanya kemungkinan transaksi gagal
    if int(metode) == 1 and harga > bayar:
        print("\nUang anda kurang!")
        x = input("\nTekan enter untuk ulangi :")
        if x == "":
            struk()
            sys.exit()
        else:
            print("\nError!")
            print("")
            print("="*50)
            txt = "Program Selesai"
            print(txt.center(50))
            print("="*50)
            sys.exit()

    Kembali = bayar - harga

    # Update data_pembeli.txt
    teks_pembeli = f"\nTanggal : {datetime.datetime.now()}\nNama : {nama_pembeli}\nUmur : {umur_pembeli}\nGender : {sex_pembeli}\nAlamat : {alamat_pembeli}\nBarang yang Dibeli : {list_belanja}\nKeterangan : {keterangan}\nDP : {dp}\nSisa : {sisa}\n"
    data_pembeli_txt.write(teks_pembeli)

    if int(metode) == 2:
        Kembali = 0

    # Update transaksi.txt
    transaksi_txt.write(f"\n{datetime.datetime.now()} Transaksi Penjualan : {list_belanja}, Metode {metode}")

    # Menampilkan Struk
    print("")
    print("="*50)
    a = "STRUK PEMBELIAN"
    print(a.center(50))
    print("="*50)
    c = "PT Sejahtera Sumber Rejeki"
    print(c.center(50))
    print("-"*50)
    print("Tanggal\t\t:",datetime.datetime.now())
    print("-"*50)
    l = len(jumlah_barang)
    i = 0
    while i < l:
        print("{0}\t({1})\t{2}\t{3}".format(barang_total[i],
        jumlah_barang[i],
        harga_total[i],
        harga_total[i]*jumlah_barang[i]))
        i += 1
    print("\t\t\t\t------------------")
    print("\t\t\tBiaya Admin :", bAdmin)
    print("\t\t\tPajak       :", pajak)
    print("\t\t\tHarga Total :", harga)
    print("\t\t\t\t------------------")
    print("Bayar\t\t:",bayar)
    print("Kembalian\t:",Kembali)
    print("Keterangan\t:\n",keterangan)
    print("Atas Nama\t:",nama_pembeli)
    print("")
    a = "Terima Kasih"
    print(a.center(50))
    print("="*50)
    b = "SAMPAI JUMPA"
    print(b.center(50))
    print("="*50)
    print("")

    # Membuat struk di txt
    file = f"Struk/Struk_{datetime.datetime.now().strftime('%Y-%m-%d (%H;%M;%S)')}.txt"
    struk_txt = open(file,"w")
    struk_txt.write("="*50)
    struk_txt.write("\n")
    a = "STRUK PEMBELIAN"
    struk_txt.write(a.center(50))
    struk_txt.write("\n")
    struk_txt.write("="*50)
    struk_txt.write("\n")
    c = "PT Sejahtera Sumber Rejeki"
    struk_txt.write(c.center(50))
    struk_txt.write("\n")
    struk_txt.write("-"*50)
    struk_txt.write("\n")
    struk_txt.write(f"Tanggal\t\t: {datetime.datetime.now()}\n")
    struk_txt.write("-"*50)
    struk_txt.write("\n")
    l = len(jumlah_barang)
    i = 0
    while i < l:
        struk_txt.write("{0}\t({1})\t{2}\t{3}\n".format(barang_total[i],
        jumlah_barang[i],
        harga_total[i],
        harga_total[i]*jumlah_barang[i]))
        i += 1
    struk_txt.write("\t\t\t\t------------------\n")
    struk_txt.write(f"\t\t\tBiaya Admin: {bAdmin}\n")
    struk_txt.write(f"\t\t\tPajak      : {pajak}\n")
    struk_txt.write(f"\t\t\tHarga Total: {harga}\n")
    struk_txt.write("\t\t\t\t------------------\n")
    struk_txt.write(f"Bayar\t\t: {bayar}\n")
    struk_txt.write(f"Kembalian\t: {Kembali}\n")
    struk_txt.write(f"Keterangan\t:\n{keterangan}\n")
    struk_txt.write(f"Atas Nama\t: {nama_pembeli}\n")
    a = "Terima Kasih"
    struk_txt.write(a.center(50))
    struk_txt.write("\n")
    struk_txt.write("="*50)
    struk_txt.write("\n")
    b = "SAMPAI JUMPA"
    struk_txt.write(b.center(50))
    struk_txt.write("\n")
    struk_txt.write("="*50)
    struk_txt.write("\n")

    # Update data stok
    i = 0
    n = len(Id)

    # Open json file untuk memodifikasi stok dan jumlah penjualan
    while i < n:
        jsonFile = open("Data/listbarang.json","r")
        data = json.load(jsonFile)
        jsonFile.close()
        temp = data["list"]
        temp[Id[i]]["Stok"] = temp[Id[i]]["Stok"] - jumlah_barang[i]
        temp[Id[i]]["Jual"] = temp[Id[i]]["Jual"] + jumlah_barang[i]

        # Write json file dengan data terbaru
        jsonFile = open("Data/listbarang.json","w+")
        jsonFile.write(json.dumps(data,indent=4))
        jsonFile.close()

        i += 1   
 
# Fungsi untuk menambahkan barang yang ingin dibeli
def programHitung():
    print("")
    print("-"*10,"Selamat Datang di Program Hitung","-"*10)
    display()
    # Looping untuk kasir
    lagi = input("Apakah ingin memasukkan barang? (y/n) :")
    while lagi == "y":
        inputBarang = int(input("Masukkan ID Barang :"))

        # Antisipasi transaksi gagal dengan memasukkan ID barang terpilih ke list Dummy
        Id.append(inputBarang)

        # Append nama barang ke list barang_total
        barang_total.append(listbarang_py["list"][inputBarang]["Nama"])

        # Append jumlah barang ke list jumlah_barang
        inputJumlah = int(input("Masukkan Jumlah Barang :"))
        jumlah_barang.append(inputJumlah)

        # Append harga ke list harga_total
        harga = listbarang_py["list"][inputBarang]["Harga"] * inputJumlah
        harga_total.append(harga)

        # cek apakah stok barang yg dipilih mencukupi
        if (listbarang_py["list"][inputBarang]["Stok"] - inputJumlah) < 0:

            print("\nStok barang yang anda pilih habis!")

            jumlah_barang.pop() # Update list jumlah belanjaan menjadi kosong
            barang_total.pop()

            x = input("\nTekan enter untuk ulangi :")

            if x == "":
                programHitung()
            else:
                print("Error!")
                print("")
                print("="*50)
                txt = "Program Selesai"
                print(txt.center(50))
                print("="*50)
                sys.exit()

        # Tanya untuk looping
        lagi = input("Apakah ingin tambah barang? (y/n) :")
    
    if lagi == "n" and len(jumlah_barang) == 0:
        print("\nError!\nList Belanja Kosong")
        print("")
        print("="*50)
        txt = "Program Selesai"
        print(txt.center(50))
        print("="*50)
        sys.exit() 
    elif lagi == "n":
        struk() # Ketika selesai memilih langsung memanggil fungsi struk
    else:
        print("\nSalah input!")
        x = input("\nTekan enter untuk ulangi (List Belanjaan Tidak Hilang!):")
        if x == "":
            programHitung()
        else:
            print("")
            print("="*50)
            txt = "Program Selesai"
            print(txt.center(50))
            print("="*50)
            sys.exit()
            
# Fungsi main menu
def mainMenu():
    # Menampilkan main menu
    print("")
    print("-"*10,"Selamat Datang di Main Menu","-"*10)
    print("\nMenu Program :")
    print("1. Program Kasir")
    print("2. Menu Stok")
    print("3. Reset Username dan Password")
    print("4. Grafik Penjualan")
    print("5. Keluar Program\n")
    x = input("Pilih menu :")
    if x == "1":
        programHitung()
    elif x == "2":
        pass
        # fungsimenu2() (belum ada)
    elif x == "3":
        pass
        # fungsimenu3() (belum ada)
    elif x == "4":
        pass
        # Import file grafik (belum ada)
    else:
        print("")
        print("="*50)
        txt = "Program Selesai"
        print(txt.center(50))
        print("="*50)
        sys.exit()

# Fungsi untuk login
def login():
    i = 0 # Percobaan ke
    print("")
    print("="*50)
    txt = "Login Kasir"
    print(txt.center(50))
    print("="*50)
    
    # Melakukan perulangan untuk percobaan login sebanyak max 3 kali
    while i != 3:
        username = input("\nMasukkan Username :")
        password = input("Masukkan Password :")
        if username == password_py["username"] and password == password_py["password"]:
            print("\nLogin Berhasil")
            mainMenu()
            break
        else:
            i += 1
            print("\nLogin Gagal\nKesempatan Login : {}".format(3-i))
    else:
        print("\nAnda Diblokir!")
        print("")
        print("="*50)
        txt = "Program Selesai"
        print(txt.center(50))
        print("="*50)
        sys.exit()

if __name__ == "__main__":
    login()

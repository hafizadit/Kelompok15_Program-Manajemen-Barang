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

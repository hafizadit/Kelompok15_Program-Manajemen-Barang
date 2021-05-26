import datetime
import sys
import json

password_json = open("Data/password.json","r")
jsondata2 = password_json.read()
password_py = json.loads(jsondata2)

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

import numpy as np
import matplotlib.pyplot as plt
import json

def grafik():
    myjson = open("Data/listbarang.json","r")
    jsondata = myjson.read()
    obj = json.loads(jsondata)

    a = obj["list"]

    nama = []
    jml = []
    cell = []
    colLabel = ("ID","Nama Produk")
   
    tabel = []

    n = 0
    while n < len(a):
        x = a[n]["ID"]
        y = a[n]["Jual"]
        z = a[n]["Nama"]
        nama.append(x)
        jml.append(y)
        cell.append([z])
        tabel.append([x,z])
        n += 1

    # Membuat tabel informasi
    table = plt.table(cellText = tabel,
    colLabels = colLabel,
    colWidths=[0.1,0.4],
    loc = "right")
    
    table.scale(0.8,1.6)
    table.set_fontsize(20)

    # Membuat grafik
    plt.subplots_adjust(left=0.057,right=0.72,bottom=0.22,top=0.75)
    x = plt.bar(nama,jml)
    plt.xticks(np.arange(0,len(a),1))
    plt.title("Grafik Penjualan")
    plt.xlabel("Nomor ID",color="red")
    plt.ylabel("Jumlah Terjual",color="red")

    infos = x.patches
    datas = jml

    for info, data in zip(infos,datas):
        letak_label = info.get_height()
        plt.text(info.get_x() + (info.get_width() / 2), letak_label , data,
            ha='center', va='bottom')
            
    plt.show()

grafik()
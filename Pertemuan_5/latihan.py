stok_barang = [15, 40, 30, 10, 25]
#1Temukan indeks dari nilai 10, lalu ubah nilai pada indeks tersebut menjadi 50.
stok_barang[3] = 50

#2.Tambahkan nilai 5 ke akhir list, kemudian urutkan list secara descending (besar ke  kecil).
stok_barang.append(5)
stok_barang.sort(reverse=True)

#3 Tampilkan jumlah total seluruh nilai dalam list tersebut. 
print(sum(stok_barang))

#4 Gunakan shorthand if (ternary) untuk menampilkan "Stok Aman" jika rata-rata nilai  dalam list > 20, jika tidak tampilkan "Waspada". 
rata_rata = sum(stok_barang)/len(stok_barang)
keterangan = "Stok aman" if rata_rata > 20 else "Waspada"
print(keterangan)


data_aktivitas = [("Diki",  88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)] 
#Lakukan perulangan pada list tersebut. Jika poin > 80, tampilkan: "[Nama]  mendapatkan predikat Gold". Jika poin 50-80, tampilkan: "[Nama] mendapatkan  predikat Silver". Di bawah itu, tampilkan: "[Nama] mendapatkan predikat Bronze" 
for nama, nilai in data_aktivitas:
    if nilai > 80:
        print(f"{nama}, mendapat predikat gold")
    
    elif nilai >= 50:
        print(f"{nama} mendapat preedikat silver")
    
    else :
        print(f"{nama} mendapat predikat bronze")

print(data_aktivitas)

ukm_coding = {"Andi", "Budi", "Caca", "Deni"} 
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"} 
#a. Tampilkan mahasiswa yang hanya mendaftar di ukm_coding saja (tidak mendaftar di  robotik). 
print(ukm_coding-ukm_robotik)
#b. Tampilkan daftar seluruh mahasiswa unik yang mendaftar di salah satu atau kedua  UKM tersebut. 
print(ukm_coding|ukm_robotik)
#c. Cek apakah "Andi" merupakan anggota dari ukm_robotik. Tampilkan hasil dalam  bentuk boolean. 
ada = "Andi" in ukm_robotik
print(ada)


gudang_pc = [ 
 {"item": "Monitor", "harga": 1500000, "stok": 5}, 
 {"item": "Keyboard", "harga": 400000, "stok": 12}, 
 {"item": "Mouse", "harga": 250000, "stok": 20} 
] 
#a. Tambahkan satu key baru bernama "kategori" dengan nilai "Aksesoris" untuk produk  Keyboard. 
tambah_key = {"kategori":"Aksesoris"}
gudang_pc[1].update(tambah_key)
print(gudang_pc[1])
#b. Tambahkan satu item baru: "Headset" dengan harga 350000 dan stok 8. 
gudang_pc.append({"item":"Headset","harga": 350000, "stok":8})
print(gudang_pc)
#c. Hitung Total Nilai Aset (Harga x Stok) untuk setiap item. Tampilkan output dengan  format: 
for uang in gudang_pc:
    aset = uang["harga"]*uang["stok"]
    print(f"item: {uang["item"]} | total aset:Rp.{aset}")


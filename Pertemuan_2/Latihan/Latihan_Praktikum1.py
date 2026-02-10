stok = [15, 50, 30, 25, 40]
#1. Tambahkan stok baru sebesar 100 ke akhir list.
stok.append(100)
print(stok)
#2. Sisipkan angka 75 di posisi indeks ke-2.
stok.insert(2,75)
print(stok)
#3. Urutkan list tersebut dari yang terbesar ke terkecil.
stok.sort()
print(stok)
#4. Hitunglah nilai rata-rata dari seluruh stok tersebut.
rata_rata = sum(stok)/len(stok)
print(rata_rata)
#5. Tampilkan isi list setelah semua perubahan dilakukan.
print(stok)


barang = ("B001", "Laptop Gaming", 15000000)
#1. Akses dan tampilkan harga barang dari tuple tersebut.
print(barang[2])
#2. Cobalah untuk mengubah harga barang menjadi 14000000.
y = list(barang)
y[2] = 14000000
barang = tuple(y)
print(barang)
#3. Gunakan teknik unpacking untuk memasukkan isi tuple ke dalam tiga variabel: kode, nama, dan harga.

(kode,nama,harga) = barang
print(kode)
print(nama)
print(harga)


tim_frontend = {"HTML", "CSS", "JavaScript", "React"}
tim_backend = {"Python", "JavaScript", "SQL",
"NodeJS"}
#1. Tentukan keahlian yang dimiliki oleh kedua tim (irisan).
tim3 = tim_frontend & tim_backend
print(tim3)
#2. Tentukan keahlian yang hanya dimiliki oleh tim_backend.
tim4 = tim_backend-tim_frontend
print(tim4)
#3. Gabungkan kedua set tersebut untuk melihat daftar total keahlian unik yang tersedia di perusahaan.
tim5 = tim_frontend.union(tim_backend)
print(tim5)



nilai_siswa = {
"S01": {"nama": "Dina", "tugas": 80, "uts": 75,
"uas": 85},
"S02": {"nama": "Abdul Harris", "tugas": 90, "uts":
88, "uas": 92},
"S03": {"nama": "Sheila", "tugas": 70, "uts": 65,
"uas": 70}
}
#1. Tambahkan data siswa baru: "S04" dengan nama "Fafa", nilai tugas 85, UTS 80, dan UAS 90.

nilai_siswa["S04"] = {
    "nama": "Fafa",
    "tugas": 85,
    "uts": 80,
    "uas": 90
}
#2. Hitunglah nilai akhir setiap siswa dengan bobot: (Tugas 20% + UTS 30% + UAS 50%) dan tampilkan hasilnya.
for data in nilai_siswa.values():
    nilai_akhir = (0.2 * data["tugas"] +
                    0.3 * data["uts"] +
                    0.5 * data["uas"])
    print(f'{data["nama"]}: {nilai_akhir}')

#3. Tampilkan nama siswa yang memiliki nilai UAS di atas 80.
for data in nilai_siswa.values():
     if data["uas"] > 80:
        print(data["nama"])
  

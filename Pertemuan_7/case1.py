"""1. Case: Sebuah sistem parkir mencatat plat nomor kendaraan yang masuk dalam
sebuah array. Kamu diminta untuk memisahkan kendaraan berdasarkan aturan
ganjil-genap.
a. Input: ["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]
b. Tugas:
1. Buat fungsi yang menerima array tersebut.
2. Identifikasi angka terakhir pada plat nomor (abaikan huruf di
belakang).
3. Pisahkan menjadi dua array baru: ganjil dan genap.
c. Logika: Mengambil karakter angka terakhir dari string dan menggunakan
operator modulus (%)."""

plat=["B 1234 ABC", "D 8888 XYZ", "A 111 TUV", "B 2022 EFG"]
genap = []
ganjil = []
for i in plat:
    if int(i.split()[1][-1]) % 2 == 0 :
        genap.append(i)

    else:
        ganjil.append(i)

print("plat genap :",genap)
print("plat ganjil:",ganjil)
    




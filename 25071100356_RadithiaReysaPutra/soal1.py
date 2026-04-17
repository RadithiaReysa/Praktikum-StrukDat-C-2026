#Fungsi Registrasi Produk dengan Serial Number 
def registrasi_gadget(merk, tipe, harga, sn):
    if harga < 1000000:
        print("error:harga harus lebih dari 1000000")
        return None
    if len(sn) < 5:
        print("error:sn harus lebih dari 5 karakter")
        return None
    return {
        "merk":merk,
        "tipe":tipe,
        1000000 : harga,
        "sn" : sn,
        "status":"tersedia"
        }

investasi = []
for i in range(1):
    merk = input("masukkan merk:")
    tipe = input("masukkan tipe:")
    harga = input("masukkan harga:")
    sn = input("masukkan sn:")
    gadget = registrasi_gadget(merk, tipe, harga, sn)
    if gadget:
        investasi.append(gadget)
    else:
        print("registrasi gagal")

for item in investasi:
    print(item)






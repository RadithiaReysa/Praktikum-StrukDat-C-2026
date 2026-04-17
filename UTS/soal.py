pengunjung_hari_ini = [
 {"id": "M001", "nama": "Rina", "usia": 20, "kategori": "Fiksi", 
"kembali": False},
 {"id": "M002", "nama": "Hendra", "usia": 23, "kategori": "Sains", 
"kembali": True},
 {"id": "M003", "nama": "Siti", "usia": 19, "kategori": "Fiksi", 
"kembali": False},
 {"id": "M004", "nama": "Taufik", "usia": 21, "kategori": "Hukum", 
"kembali": True},
 {"id": "M005", "nama": "Yuni", "usia": 18, "kategori": "Sains", 
"kembali": False},
 {"id": "M006", "nama": "Bagas", "usia": 22, "kategori": "Hukum", 
"kembali": False},
]
def tampilkan_pengunjung(data):
    print("id\t|nama\t|usia\t|kategori\t|status kembali")
    for x in data:
        print(x["id"],"\t",x["nama"],"\t",x["usia"],"\t",x["kategori"],"\t",x["kembali"])
    return
tampilkan_pengunjung(pengunjung_hari_ini)
    
def filter_belum_kembali(data):
    status = [x["nama"] for x in data if x["kembali"]== False ]
    print(status)
    print("Total belum kembali:",len(status))
    return
print("======Data Belum Kembali======")
filter_belum_kembali(pengunjung_hari_ini)

def info_perpustakaan():
    print("Info Perpustakaan:")
    print("Nama   : Perpustakaan Kampus Terpadu")
    print("Alamat : Jl. Pendidikan No. 5, Pekanbaru")
    print("Telp   : 0761-54321")
    return
print("\n")
info_perpustakaan()

def rekap_kategori(data):
    list_kategori = []
    for x in data:
        list_kategori.append(x["kategori"])
    
    unik = set(list_kategori)
    print("Kategori Buku Unik:",unik)
    print("Jumlah kategori:",len(unik))

    frek={}
    for x in list_kategori:
        if x in frek:
            frek[x] +=1
        else:
            frek[x] = 1
    print(frek)
        
    maks = max(frek.values())

    for k,v in frek.items():
        if v == maks:
            print(k,"\t:",v,"Pengunjung")
    return

rekap_kategori(pengunjung_hari_ini)
    


class Pengunjung:
    jumlah = 0
    def __init__(self,id,nama,kategori):
        self.__id=id
        self.__nama=nama
        self.__kategori=kategori
        self.jumlah +=1

    def get_id(self):
        return self.id
    
    def get_nama(self):
        return self.nama
    
    def get_kategori(self):
        return self.kategori
    
    def tampilkan_info(self):
        print("ID      :",self.__id)
        print("Nama    :",self.__nama,)
        print("Kategori:",self.__kategori)
        
    @staticmethod
    def hitung_pengunjung():
        return Pengunjung.jumlah
    
class PengunjungPrioritas(Pengunjung):
    def __init__(self, id, nama, kategori,prioritas):
        super().__init__(id, nama, kategori)
        self.prioritas = prioritas

    def tampilkan_info(self):
        print("ID      :",self.__id)
        print("Nama    :",self.__nama,)
        print("Kategori:",self.__kategori)
        print("Prioritas:",self.prioritas)
        if self.prioritas == "Mendesak":
            print("** Layani segera! **")


    



#no 4
class Node:
    def __init__(self):
        
        pass
print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M001 - Rina | Fiksi")
print("[2] M002 - Hendra | Sains")
print("[3] M003 - Siti | Fiksi")
print("[4] M004 - Taufik | Hukum")
print("Total antrian: 4")
print("Memanggil pengunjung berikutnya...")
print("Silakan masuk: Rina (M001) - Fiksi")
print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M003 - Siti | Fiksi")
print("[3] M004 - Taufik | Hukum")
print("Total antrian: 3")
print("Menghapus pengunjung dengan ID M003...")
print("Siti (M003) berhasil dihapus dari antrian.")
print("===== ANTRIAN PEMINJAMAN =====")
print("[1] M002 - Hendra | Sains")
print("[2] M004 - Taufik | Hukum")
print("Total antrian: 2")
print("Mencari 'Taufik'...")
print("Ditemukan: M004 - Taufik | Hukum (posisi ke-2)")
print("Total antrian: 2")

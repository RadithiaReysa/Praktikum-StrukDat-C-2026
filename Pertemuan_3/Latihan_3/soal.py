class Celana:
    def __init__(self,jenis,warna,Harga):
        self.jenis = jenis
        self.warna = warna
        self.Harga = Harga

    def spesifikasi(self):
        print(f"Jenis Mobil :{self.jenis} Berwarna:{self.warna} Harga keluaran:{self.Harga}")

    def ubah_warna(self, NewWarna):
        self.warna = NewWarna
        print(f"Warna diubah menjadi {NewWarna}")

Nomor1 = Celana("Jeans","Dongker","45.000")
Nomor2 = Celana("Celana Panjang","Putih","75.000")
Nomor3 = Celana("Celana Pendek","Hitam","40.000")

Nomor1.spesifikasi()
Nomor1.ubah_warna("Biru")
Nomor2.spesifikasi()
Nomor2.ubah_warna("Hitam")
Nomor3.spesifikasi()
Nomor3.ubah_warna("Putih")

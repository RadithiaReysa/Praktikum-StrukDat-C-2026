from kurs import kurs
from konverter import konversi
from tabulate import tabulate

print("=== KONVERTER MATA UANG ===")

# Tabel kurs
data_tabel = []
for kode, nilai in kurs.items():
    data_tabel.append([kode, f"{nilai:,}".replace(",", ".")])

print(tabulate(data_tabel, headers=["Kode", "Kurs"], tablefmt="pretty", colalign=("left","right")))

# Input user
daftar = "IDR/USD/EUR/SGD/JPY"

dari = input(f"Dari ({daftar}): ").upper()
ke = input(f"Ke ({daftar}): ").upper()
jumlah = float(input("Jumlah: "))

# hitung konversi
hasil = konversi(dari, ke, jumlah)

# tampilkan hasil
print(f"{jumlah:,.0f} {dari} ".replace(",", "."),
      "=",
      f"{hasil:.2f}",ke)
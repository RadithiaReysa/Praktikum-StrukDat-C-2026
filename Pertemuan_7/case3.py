"""Layanan Valet VIP tetap memungkinkan kendaraan untuk menyalip.
Namun, karena keterbatasan sistem (Singly Linked List), petugas hanya bisa
melihat kendaraan di depannya. Kendaraan VIP baru dapat disisipkan tepat di
belakang kendaraan VIP tertentu yang sudah ada dalam antrean. Karena hanya
satu arah, untuk pengecekan urutan, petugas harus membacanya dari kendaraan
paling depan hingga paling belakang.
a. Tugas:
1. Gunakan struktur Singly Linked List (hanya memiliki pointer next).
2. Buat fungsi sisipkan_vip(plat_baru, plat_target):
Mencari plat_target dalam antrean, lalu menyisipkan
plat_baru tepat setelahnya.
3. Buat fungsi tampilkan_antrean() untuk menunjukkan urutan
kendaraan dari depan ke belakang.
b. Logika: Menelusuri list dari head untuk mencari plat_target. Setelah
ditemukan, buat node baru, hubungkan next dari node baru ke next milik
target, lalu ubah next milik target ke node baru."""

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def Sisipkan_VIP(head, newPlat, position):
  if position == 1:
    newPlat.next = head
    return newPlat

  currentNode = head
  for _ in range(position - 2):
    if currentNode is None:
      break
    currentNode = currentNode.next

  newPlat.next = currentNode.next
  currentNode.next = newPlat
  return head

def TampilkanData(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

node1 = Node("B 1234 ABC")
node2 = Node("D 8888 XYZ")
node3 = Node("A 111 TUV")
node4 = Node("B 2022 EFG")

node1.next = node2
node2.next = node3
node3.next = node4

print("Original list:")
TampilkanData(node1)

newnode = Node("B 2133 DSA")
Sisipkan_VIP(node1,newnode,2)
print("\nAfter insertion:")
TampilkanData(node1)

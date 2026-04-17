"""Kendaraan yang sudah selesai urusan harus keluar melalui satu pintu yang
sama. Karena ini antrean, kendaraan yang pertama datang harus pertama keluar
(FIFO). Namun, karena ada kendala teknis, terkadang ada kendaraan di urutan
tertentu yang "mogok" dan harus dihapus dari daftar antrean secara paksa.
a. Tugas:
1. Buat struktur Node dan LinkedList.
2. Buat fungsi tambahKendaraan(plat) untuk menambah
kendaraan ke akhir list (Tail).
3. Buat fungsi hapusKendaraan(plat) untuk menghapus kendaraan
tertentu jika ia mogok di tengah antrean.

b. Logika: Melakukan traversal (penelusuran) dari head hingga menemukan
plat yang cocok, lalu menyambungkan node sebelumnya langsung ke node
sesudahnya."""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverseAndPrint(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def tambahKendaraan(head,plat):
    currentNode = head
    while currentNode.next:
        currentNode = currentNode.next

    currentNode.next = plat


def hapusKendaraan(head,plathapus):
    currentNode = head
    if head == plathapus:
            return head.next

    currentNode = head
    while currentNode.next and currentNode.next != plathapus:
            currentNode = currentNode.next

    if currentNode.next is None:
             return head

    currentNode.next = currentNode.next.next


node1 = Node("B 1234 ABC")
node2 = Node("D 8888 XYZ")
node3 = Node("A 111 TUV")
node4 = Node("B 2022 EFG")

node1.next = node2
node2.next = node3
node3.next = node4

print("Original list:")
traverseAndPrint(node1)

node5 = Node("B 2133 DSA")
tambahKendaraan(node1,node5)
print("\nAfter insertion:")
traverseAndPrint(node1)

hapusKendaraan(node1, node2)
print("\nAfter deletion:")
traverseAndPrint(node1)


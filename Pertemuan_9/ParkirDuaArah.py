class Node:
    def __init__(self, plat):
        self.plat = plat
        self.prev = None # pointer ke node sebelumnya
        self.next = None # pointer ke node berikutnya

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_kendaraan(self,plat):
        new_node = Node(plat)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def tampilkan_maju(self):
        temp = self.head
        print("Tampilan Maju:")
        while temp:
            print(temp.plat)
            temp = temp.next

    def tampilkan_mundur(self):
        temp = self.tail
        print("Tampilan Mundur:")
        while temp:
            print(temp.plat)
            temp = temp.prev

    def hapus_kendaraan(self,plat):
        temp = self.head

        while temp:
            if plat == plat:
                #hapus diawal
                if temp == self.head:
                    self.head = temp.next
                    if self.head:
                        self.head.prev = None

                #hapus diakhir
                elif temp == self.tail:
                    self.tail = temp.prev
                    if self.tail:
                        self.tail.next = None
                
                #hapus ditengah
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev

                print(f"Kendaraan dengan plat {plat} telah dihapus")
                return
            temp = temp.next

        print("Kendaraan tidak ada")

#Soal Nomor 1     
linked =DoubleLinkedList()
linked.tambah_kendaraan("B 1234 ABC")
linked.tambah_kendaraan("D 5678 XYZ")
linked.tambah_kendaraan("A 9999 TUV")
linked.tampilkan_maju()
print()
linked.tampilkan_mundur()





class Node:
  def __init__(self, nama,keluhan):
    self.nama = nama
    self.keluhan = keluhan
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def enqueue(self,pasien,keluhan):
    new_node = Node(pasien,keluhan)
    if self.tail is None:
      self.head = self.tail = new_node
      self.length += 1
      return
    self.tail.next = new_node
    self.tail = new_node
    self.length += 1
    

  def dequeue(self):
    if self.isEmpty():
      return "ANTRIAN KOSONG"
    temp = self.head
    self.head = temp.next
    self.length -= 1
    if self.head is None:
      self.tail = None
    return temp.nama, temp.keluhan

  def peek(self):
    if self.isEmpty():
      return "ANTRIAN KOSONG"
    return self.head.nama , self.head.keluhan

  def isEmpty(self):
    return self.length == 0

  def size(self):
    return self.length

  def printQueue(self):
    temp = self.head
    count =1
    while temp:
      print(f"{temp.nama} -> {temp.keluhan} (No.Antrian:{count})" )
      count+=1
      temp = temp.next
    print()

  def clear(self):
    while self.head:
      self.dequeue()

# Create a queue
Antrean = Queue()
print("====================================")
print("SISTEM ANTRIAN POLI UMUM")
print("RS Sehat Bersama")
print("====================================")

print("Apakah antrian kosong: ", Antrean.isEmpty())
Antrean.enqueue("BUDI","demam tinggi")
Antrean.enqueue("ANI","batuk pilek")
Antrean.enqueue("CITRA","sakit kepala")
print()
print("ANTRIAN: ")
Antrean.printQueue()
print("Jumlah Pasien: ", Antrean.size())
print("Pasien Berikutnya: ", Antrean.peek())
print("Dokter Memanggil: ", Antrean.dequeue())

Antrean.enqueue("DODI","nyeri perut")
print()
print("ANTRIAN: ")
Antrean.printQueue()
print("Dokter Memanggil: ", Antrean.dequeue())
print("Jumlah Pasien: ", Antrean.size())
print()
print("Sesi poliklinik selesai. Antrian dikosongkan.")
Antrean.clear()
print("Apakah Antrian Kosong: ", Antrean.isEmpty())

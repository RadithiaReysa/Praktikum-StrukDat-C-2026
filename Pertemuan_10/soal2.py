#Menggunakan linkedlist
class Node:
    def __init__(self, url):
        self.url = url
        self.next = None
        
class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0 # Variabel bantuan untuk melacak ukuran

    def is_empty(self):
        # Tulis kode di sini (Petunjuk: periksa apakah top bernilai None)
        return self.top == None
        
    def push(self, url):
        # Tulis kode di sini
        # 1. Buat Node baru
        Node_baru = Node(url)
        # 2. Hubungkan 'next' node baru ke 'top' saat ini
        if self.top:
            Node_baru.next = self.top
        # 3. Jadikan node baru sebagai 'top' yang baru
        self.top = Node_baru
        # 4. Tambahkan nilai 'count'
        self.count +=1

    def pop(self):
        # Tulis kode di sini
        # 1. Periksa is_empty()
        if self.is_empty():
            return "Riwayat kosong"
        # 2. Simpan url dari 'top' saat ini
        popped_node = self.top
        # 3. Geser 'top' ke node berikutnya (top = top.next)
        self.top = self.top.next
        # 4. Kurangi nilai 'count'
        self.count -=1
        # 5. Kembalikan url yang disimpan
        return popped_node.url

    def peek(self):
        # Tulis kode di sini (Petunjuk: kembalikan nilai url dari 'top')
        if self.is_empty():
            return "Riwayat kosong"
        return self.top.url

    def size(self):
        # Tulis kode di sini (Petunjuk: kembalikan nilai variabel 'count')
        return self.count
    
    def traverseAndPrint(self):
        currentNode = self.top
        while currentNode:
            print(currentNode.url, end=" -> ")
            currentNode = currentNode.next
        print()

myStack = StackLinkedList()
myStack.push('google.com')
myStack.push('w3schools.com')
myStack.push('youtube.com')

print("Stack Linked List:", end="")
myStack.traverseAndPrint()
print("Peek:", myStack.peek())
print("Pop:", myStack.pop())
print("LinkedList after Pop:", end="")
myStack.traverseAndPrint()
print("isEmpty:", myStack.is_empty())
print("Size:", myStack.size())
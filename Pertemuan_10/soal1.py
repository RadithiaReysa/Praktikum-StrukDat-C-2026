#Simulasi Riwayat Navigasi Browser
#menggunakan class
class StackList:
    def __init__(self):
        self.items = [] # Menggunakan list bawaan Python
    def is_empty(self):
        # Tulis kode di sini
        return len(self.items) == 0

    def push(self, url):
        # Tulis kode di sini (Petunjuk: gunakan append)
        self.items.append(url)

    def pop(self):
        # Tulis kode di sini (Petunjuk: pastikan tidak kosong, lalu gunakan pop)
        if self.is_empty():
          return None
        return self.items.pop()

    def peek(self):
        # Tulis kode di sini (Petunjuk: kembalikan elemen indeks terakhir [-1])
        if self.is_empty():
          return "Stack is empty"
        return self.items[-1]

    def size(self):
        # Tulis kode di sini (Petunjuk: gunakan len())
        return len(self.items)

myStack = StackList()

myStack.push('google.com')
myStack.push('w3schools.com')
myStack.push('youtube.com')

print("Stack: ", myStack.items)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.items)
print("Peek: ", myStack.peek())
print("is_empty: ", myStack.is_empty())
print("Size: ", myStack.size())
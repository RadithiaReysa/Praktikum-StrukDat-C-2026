class Node:
    def __init__(self,id,judul):
        self.id = id
        self.judul = judul
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, node, id, judul):
        if node is None:
            print(f"Berhasil memasukkan: ID {id} - {judul}")
            return Node(id, judul)

        if id < node.id:
            node.left = self.insert(node.left, id, judul)
        else:
            node.right = self.insert(node.right, id, judul)

        return node

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"{node.id} - {node.judul}")
            self.inorder(node.right)

    def search(self, node, id):
        if node is None:
            print(f"Mencari ID {id}... Data tidak ditemukan.")
            return

        if id == node.id:
            print(f"Mencari ID {id}... Ditemukan! Judul: {node.judul}")
        elif id < node.id:
            self.search(node.left, id)
        else:
            self.search(node.right, id)

    def get_min(self, node):
        while node.left:
            node = node.left
        return node.id

    def get_max(self, node):
        while node.right:
            node = node.right
        return node.id

    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))


print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
print("="*70)

bst = BST()


bst.root = bst.insert(bst.root, 50, "Dasar Pemrograman")
bst.root = bst.insert(bst.root, 30, "Struktur Data")
bst.root = bst.insert(bst.root, 70, "Kecerdasan Buatan")
bst.root = bst.insert(bst.root, 20, "Matematika Diskrit")
bst.root = bst.insert(bst.root, 40, "Basis Data")
bst.root = bst.insert(bst.root, 60, "Jaringan Komputer")
bst.root = bst.insert(bst.root, 80, "Sistem Operasi")


print("\n[INFO] Koleksi Buku (In-Order Traversal):")
bst.inorder(bst.root)


print()
bst.search(bst.root, 60)
bst.search(bst.root, 100)


print(f"\nID Terkecil: {bst.get_min(bst.root)}")
print(f"ID Terbesar: {bst.get_max(bst.root)}")


print(f"Tinggi (Height) Tree: {bst.height(bst.root)}")

print("="*70)
print("Simulasi Selesai!")
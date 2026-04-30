class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def insert_manual():
    root = TreeNode('A')
    nodeB = TreeNode('B')
    nodeC = TreeNode('C')
    nodeD = TreeNode('D')
    nodeE = TreeNode('E')
    nodeF = TreeNode('F')

    root.left = nodeB
    root.right = nodeC

    nodeB.left = nodeD
    nodeB.right = nodeE

    nodeC.right = nodeF
    return root



def traverse_preorder(node):
    if node:
        print(node.data, end="->")
        traverse_preorder(node.left)
        traverse_preorder(node.right)

def traverse_inorder(node):
    if node:
        traverse_preorder(node.left)
        print(node.data, end="->")
        traverse_preorder(node.right)
def traverse_postorder(node):
    if node:
        traverse_preorder(node.left)
        traverse_preorder(node.right)
        print(node.data, end="->")

def get_leaf_nodes(node, leaves):
    if node:
        if node.left is None and node.right is None:
            leaves.append(node.data)
        get_leaf_nodes(node.left, leaves)
        get_leaf_nodes(node.right, leaves)

root = insert_manual()
print("SISTEM AUDIT DISTRIBUSI 'CEPAT SAMPAI'")
print("="*30)
print("Membangun Struktur Gudang...")
print("Struktur berhasil dibuat.")
print()
print("Pre-Order:")
traverse_preorder(root)
print()
print("InOrder:")
traverse_inorder(root)
print()
print("Postorder:")
traverse_postorder(root)

leaves = []
get_leaf_nodes(root,leaves)
print("\nGudang Ujung (Leaf Nodes):",leaves)
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

# --- 1. Hàm Chèn ---
def insert(root, key):
    if root is None:
        root = Node(key)
        return root
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

# --- 2. Hàm Tìm kiếm ---
def search(root, key):
    # Trả về True nếu tìm thấy, False nếu không
    if root is None:
        return False
    if root.val == key:
        return True
    
    if key < root.val:
        return search(root.left, key)
    else:
        return search(root.right, key)

# --- 3. Hàm Duyệt (In ra để kiểm tra) ---
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" -> ")
        inorder(root.right)

# --- CHẠY THỬ ---
# Tạo nút gốc đầu tiên là 50
root = Node(50)

# Chèn các số lộn xộn vào: 30, 20, 40, 70, 60, 80
elements = [30, 20, 40, 70, 60, 80]
for e in elements:
    insert(root, e)
print("Cây sau khi sắp xếp (Duyệt In-order):")
inorder(root)
print("Kết thúc")
# Thử tìm kiếm
print("\nTìm số 60:", search(root, 60)) # Mong đợi: True
print("Tìm số 99:", search(root, 99)) # Mong đợi: False
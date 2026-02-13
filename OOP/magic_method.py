class ViTienThuong:
    def __init__(self, so_du):
        self.so_du = so_du

    # Phải gọi hàm này mới in ra được chuỗi đẹp
    def in_thong_tin(self):
        return f"Ví có: {self.so_du} VND"

    # Phải gọi hàm này để cộng
    def cong_tien(self, vi_khac):
        return ViTienThuong(self.so_du + vi_khac.so_du)

    # Phải gọi hàm này để so sánh
    def giong_nhau(self, vi_khac):
        return self.so_du == vi_khac.so_du

# --- SỬ DỤNG ---
vi_1 = ViTienThuong(100)
vi_2 = ViTienThuong(200)

# 1. In ra
print(vi_1.in_thong_tin())  # Phải nhớ gọi .in_thong_tin()

# 2. Cộng tiền
vi_tong = vi_1.cong_tien(vi_2) # Nhìn khá dài dòng và giống Java/C++
print(vi_tong.in_thong_tin())

# 3. So sánh
if vi_1.giong_nhau(vi_2): # Không thể dùng dấu ==
    print("Bằng nhau")
else:
    print("Khác nhau")

class ViTienMagic:
    def __init__(self, so_du):
        self.so_du = so_du

    # __str__: Tự động chạy khi gọi print()
    def __str__(self):
        return f"Ví có: {self.so_du} VND"

    # __add__: Tự động chạy khi dùng dấu +
    def __add__(self, other):
        return ViTienMagic(self.so_du + other.so_du)

    # __eq__: Tự động chạy khi dùng dấu == (equal)
    def __eq__(self, other):
        return self.so_du == other.so_du

# --- SỬ DỤNG ---
vi_1 = ViTienMagic(100)
vi_2 = ViTienMagic(200)

# 1. In ra (Gọn hơn nhiều)
print(vi_1)  # Tự động gọi __str__, in ra: "Ví có: 100 VND"

# 2. Cộng tiền (Dùng dấu + tự nhiên)
vi_tong = vi_1 + vi_2  # Tự động gọi __add__
print(vi_tong)         # In ra: "Ví có: 300 VND"

# 3. So sánh (Dùng dấu == tự nhiên)
if vi_1 == vi_2:       # Tự động gọi __eq__
    print("Bằng nhau")
else:
    print("Khác nhau")
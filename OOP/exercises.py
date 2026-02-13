class SanPham:
    def __init__(self, id, ten, giaban, cannang):
        self.id = id
        self.ten = ten
        self.giaban = giaban
        self.cannang = cannang
    @property
    def giaban(self):
        return self.__giaban
    @giaban.setter
    def giaban(self, value):
        if value<0:
            raise ValueError("Giá bán không thể âm")
        self.__giaban = value
    @property
    def cannang(self):
        return self.__cannang
    @cannang.setter
    def cannang(self, value):
        if value<0:
            raise ValueError("Cân nặng không thể âm")
        self.__cannang = value
class KhachHang:
    def __init__(self, ID, ten, vi):
        self.id = ID
        self.ten = ten
        self.vi = vi
    def naptien(self, value):
        if value <= 0:
            return f"Số tiền nạp phải lớn hơn 0"
        else:
            self.vi += value
    def ruttien(self, value):
        if value > self.vi:
            raise ValueError("Không thể rút số tiền lớn hơn số dư")
        else:
            self.vi -= value
class KhachVip(KhachHang):
    def __init__(self, ID, ten, vi):
        super().__init__(ID, ten, vi)
    def get_discount_rate(self):
        return 0.1
def binary_search(a, y):
    left = 0
    right = len(a) - 1
    while (left <= right ):
        mid = (left+right)//2
        if a[mid] == y:
            return 1
        elif a[mid]<y:
            left = mid+1
        else:
            right = mid-1
    return 0
N, Q = map(int, input().split())
a = set(map(int, input().split()))
for i in range (Q):
    y = int(input())
    if binary_search(a, y):
        print("YES")
    else:
        print("NO")
        
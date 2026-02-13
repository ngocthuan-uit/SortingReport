class HashTable:
    def __init__(self):
        self.max=100
        self.arr = [None for i in range (self.max)]
    def get_hash(self,key):
        h=0
        for i in key:
            h+=ord(i)
        return h % self.max
    def set_item(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value
    def get_item(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    def del_item(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
t = HashTable()
print(t.get_hash("march 6"))
t.set_item("march 6", 130)
t.del_item("march 6")
print(t.get_item("march 6"))
a=[1,3,4,56,7,8]
a.append(100)
print(sum(a[:2])/2)
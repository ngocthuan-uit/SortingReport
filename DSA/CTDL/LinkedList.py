class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
class LinkedList():
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    def print(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            itr = self.head
            llstr = ""
            while itr:
                llstr += str(itr.data) + " --> "
                itr = itr.next
            print(llstr)
    def insert_at_end(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = node
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
        else:
            count = 0
            itr = self.head
            while (index - count != 1):
                count += 1
                itr = itr.next
            itr.next = itr.next.next
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index==0:
            self.head = Node(data, self.head)
            return
        count = 0
        itr = self.head
        while (index - count != 1):
            count +=1
            itr = itr.next
        itr.next = Node(data, itr.next)
        
ll = LinkedList()
ll.insert_values(["banana", "mango", "grapes", "orange"])
ll.insert_at(2, "fug")
ll.print()
print(ll.get_length())

        

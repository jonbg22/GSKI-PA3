class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

        self.current = None
        self.size = 0

    def insert(self, data):
        new_node = Node(data)
        if self.size == 0:
            self.head.next = new_node
            self.tail.prev = new_node
            new_node.next = self.tail
            new_node.prev = self.head
            self.current = new_node
        else:
            self.current.prev.next = new_node
            # self.current.next.prev = new_node
            new_node.next = self.current
            new_node.prev = self.current.prev
            self.current.prev = new_node
            self.current = new_node

        self.size += 1
            

    def remove(self):
        if self.current == None:
            return
        elif self.size == 1:
            self.head.next = self.tail
            self.tail.prev = self.head
            self.current = None
        else:
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            if self.current.next == self.tail:
                self.current = None
            else:
                self.current = self.current.next
        self.size -= 1
        

    def get_value(self):
        if self.current == None:
            return
        return self.current.data

    def move_to_next(self):
        if self.current == None:
            return
        if self.current.next == self.tail:
            return
        self.current = self.current.next

    def move_to_prev(self):
        if self.current == None:
            return
        if self.current.prev == self.head:
            return
        self.current = self.current.prev

    def move_to_pos(self, pos):
        if 0 > self.size or abs(pos) > self.size-1:
            return
        
        if pos >= 0:
            cur = self.head.next
            for _ in range(pos):
                cur = cur.next
        elif pos < 0:
            cur = self.tail.prev
            for _ in range(abs(pos)):
                cur = cur.prev
        self.current = cur 

    def clear(self):
        self.current = None
        self.head.next = self.tail
        self.tail.prev = self.tail
        self.size = 0

    def get_first_node(self):
        if self.size == 0:
            return None
        return self.head.next

    def get_last_node(self):
        if self.size == 0:
            return None
        return self.tail.prev

    def partition(self, low, high):
        # print("Entered Partition with low:",low.data,"high:",high.data)
        ind = 0
        self.current = low
        while True:
            # print("Index:",ind)
            print(self.current.data)
            # print("Before Change:",self.current.data, i.data)
            if self.get_value() <= low.data and self.current != low:
                val = self.get_value()
                self.remove()
                self.current = low
                self.insert(val)
            if self.current == high or ind == 50:
                print("Broke")
                break
            self.move_to_pos(ind+1)
            ind += 1
        self.current = low


    def quick_sort(self,low,high):
        if low != high:
            self.partition(low,high)
            pi = self.current
            self.quick_sort(low,pi.prev)
            self.quick_sort(pi.next,high)


    def sort(self):
        self.quick_sort(self.get_first_node(),self.get_last_node())        
        
        
    def is_sorted(self):
        cur = self.head.next
        while cur.next != self.tail:
            if cur.data > cur.next.data:
                return False
            cur = cur.next
        return True

    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        cur_node = self.head.next
        while cur_node != self.tail:
            ret_str += f"{cur_node.data} "
            cur_node = cur_node.next
        return ret_str


def randomNumbers(amount,low,high):
    from random import randint
    while amount > 0:
        yield randint(low,high)
        amount -= 1
        


if __name__ == "__main__":
    #create tests here if you want
    dll = DLL()
    # for num in [6, 3, 1, 14, 17, 1, 10]:
    for num in randomNumbers(10,1,20):
        dll.insert(num)
    print(dll)
    dll.partition(dll.get_first_node(),dll.get_last_node())
    print(dll)
    print(dll.get_value())
    # dll.sort()
    # print(dll)

if __name__ == "__main__" and False:
    dll = DLL()
    for item in  ["A","B1","C","A","B2"]:
        dll.insert(item)

    print(dll)
    dll.partition(dll.get_first_node(),dll.get_last_node())
    print(dll)
    print(dll.get_value())
    
     



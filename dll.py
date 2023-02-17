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
            self.current.next.prev = new_node
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
                self.current = self.current.prev
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
        if 0 > self.size or pos > self.size-1:
            return
        cur = self.head.next
        for _ in range(pos):
            cur = cur.next
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
        pivot = high.data
        i = low
        self.current = low
        while self.current != high:
            # print("Before Change:",self.current.data, i.data)
            if self.get_value() <= pivot:
                self.current.data,i.data = i.data,self.current.data # swaps values
                i = i.next
            # print("After Change:",self.current.data, i.data)
            self.move_to_next()

        high.data,i.data = i.data,high.data # swaps values
        
        self.current = i

    def quick_sort(self,low,high):
        if high.next != low:
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
    while amount > 0:
        yield randint(low,high)
        amount -= 1
        


if __name__ == "__main__":
    #create tests here if you want
    dll = DLL()
    from random import randint
    for num in randomNumbers(7,1,20):
        dll.insert(num)
    dll.move_to_pos(6)
    print(dll.get_value())
    print(dll)
    dll.remove()
    print(dll)
    dll.remove()
    print(dll)
    dll.remove()
    print(dll)
     



class Node:
    def __init__(self, data = None, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

class DLL:
    def __init__(self):
        self.head = Node("Head")
        self.tail = Node("Tail")

        self.head.next = self.tail
        self.tail.prev = self.head

        self.current = None
        self.size = 0

    def insert(self, data):
        new_node = Node(data)
        if self.head.next == self.tail:
            self.tail.prev.next = new_node
            new_node.prev = self.tail.prev
            self.tail.prev = new_node
            new_node.next = self.tail
            self.current = new_node
        elif self.current is None:
            return
        else:
            self.current.prev.next = new_node
            new_node.next = self.current
            new_node.prev = self.current.prev
            self.current.prev = new_node
            self.current = new_node

        self.size += 1
            

    def remove(self):
        if self.current is None or self.current == self.head or self.current == self.tail:
            return
        elif self.size == 1:
            self.head.next = self.tail
            self.tail.prev = self.head
            self.current = None
        else:
            self.current.prev.next = self.current.next
            self.current.next.prev = self.current.prev
            self.current = self.current.next
        self.size -= 1
        

    def get_value(self):
        if self.current is None:
            return
        return self.current.data

    def move_to_next(self):
        if self.current is None or self.current.next is None:
            return
        else:
            self.current = self.current.next

    def move_to_prev(self):
        if self.current is None or self.current.prev == self.head:
            return
        else:
            self.current = self.current.prev

    def move_to_pos(self, pos):
        if pos < 0 or pos > self.size:
            return
            
        cur = self.head.next
        for _ in range(pos):
            cur = cur.next

        self.current = cur 

    def clear(self):
        self.head.next = self.tail
        self.tail.prev = self.head
        self.current = None
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
        if low.next == self.tail or low.next == None:
            return
        cur = low.next
        while cur != high.next:
            if cur == None:
                break
            if cur.data < low.data:
                moved = Node(cur.data)
                self.current = cur
                self.remove()
                low.prev.next = moved
                moved.next = low
                moved.prev = low.prev
                low.prev = moved
                self.size += 1
                
            cur = cur.next
        self.current = low

    def is_sorted(self):
        cur = self.head.next
        while cur.next != self.tail:
            if cur.data > cur.next.data:
                return False
            cur = cur.next
        return True    

    def quick_sort(self,low,high):
        if low != high and low != None and low != high.next:
            self.partition(low,high)
            pi = self.current
            self.quick_sort(low,pi.prev)
            self.quick_sort(pi.next,high)


        

    def sort(self):
        self.quick_sort(self.get_first_node(),self.get_last_node())    
        self.current = self.head.next  
        
        
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

    def print_backwards(self):
        print_string = ""
        node = self.tail.prev
        while node != self.head:
            print_string += str(node.data) + " "
            node = node.prev
        print(print_string)

def randomNumbers(amount,low,high):
    from random import randint
    while amount > 0:
        yield randint(low,high)
        amount -= 1
        


if __name__ == "__main__":
    #create tests here if you want
    dll = DLL()
    # for num in [6, 3, 1, 14, 17, 1, 10]: # 10 1 17 14 1 3 6 
    for num in randomNumbers(3,1,30):
        dll.insert(num)
    print(dll)
    # dll.partition(dll.get_first_node(),dll.get_last_node())
    # dll.sort()
    dll.move_to_prev()
    print(dll.get_value())
    dll.move_to_prev()
    print(dll.get_value())
    dll.move_to_prev()
    print(dll.get_value())
    dll.insert("A")
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
    
     



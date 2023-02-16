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
        if self.current == None:
            self.head.next = new_node
            self.tail.prev = new_node
            self.current = new_node
            new_node.prev = self.head
            new_node.next = self.tail
        elif self.current.next == self.tail:
            self.tail.prev = new_node
            new_node.next = self.tail
            new_node.prev = self.current
            self.current.next = new_node
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
            if self.current.prev == self.head:
                self.current = self.head.next
            else:
                self.current = self.current.prev
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
        self.move_to_pos(0)
        while self.current != high:
            print("Before Change:",self.current.data, i.data)
            if self.get_value() <= pivot:
                self.current.data,i.data = i.data,self.current.data # swaps values
                i = i.next
            print("After Change:",self.current.data, i.data)
            self.move_to_next()

            
    def sort(self):
        pass

    def __len__(self):
        return self.size

    def __str__(self):
        ret_str = ""
        cur_node = self.head.next
        while cur_node != self.tail:
            ret_str += f"{cur_node.data} "
            cur_node = cur_node.next
        if ret_str == "":
            return "List is empty"
        return ret_str


def randomNumbers(amount,low,high):
    while amount > 0:
        yield randint(low,high)
        amount -= 1
        


if __name__ == "__main__":
    #create tests here if you want
    dll = DLL()
    from random import randint
    for num in randomNumbers(5,1,100):
        dll.insert(num)
    print(dll)
    dll.partition(dll.get_first_node(),dll.get_last_node())
    print(dll)



class Library:
    data:object
def __add__(self, other):
    if not self.data.get(other.author):
        self.data[other.author] = [other]
        return self
    self.data[other.author].append(other)

    return self

def __sub__(self, other):
    if other.author not in self.data.keys():
        return
    
    if not len(self.data[other.author]):
        del self.data[other.author]
        return self
    
    self.data.pop(other.author)
    return self

class List():
    def __add__(self, value):
        self.append(value)
        return self
    
    def __sub__(self, value):
        del self[self.index(value)]
        return self
    
    def __mul__(self, value):
        self.append(value)

class Node:
    data = None
    next = None

    def __init__(self,data):
        self.data = data

class LinkedList:
    start = None
    end = None

    def __mul__(self, data):
        temp = self.start
        while (temp):
            if data == temp.data:
                return temp
            temp = temp.next

    def __add__(self, obj):
        new_node = Node(obj)
        if self.start is None:
            self.start = new_node
            return
        
        current_node = self.start 
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    def __sub__(self, index: int):
        if self.start == None:
            return
        
        current_node = self.start
        position = 0
        if position == index:
            self.start = self.start.next
        else:
            while(current_node != None and position + 1 != index):
                position += 1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next

    def __len__(self):
        temp = self.start
        count = 0
        while (temp):
            count += 1
            temp = temp.next
        return count
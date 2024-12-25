class Resource:
    def __init__(self, name:str, resource_type:str):
        self.name = name
        self.resource_type = resource_type

    def __del__(self):
        print(f"Ресурс {self.name} типа {self.resource_type} удалён.")

r1 = Resource('Соединение1', "подключение к базе данных")
r2 = Resource('Соединение2', "подключение к базе данных")

for _ in range(1, 11):
    print(_)
    if _ == 5: 
        del r2

class Node:
    data = None
    next = None

class LinkedList:
    start = None
    end = None

    def len(self):
        temp = self.start
        count = 0
        while(temp):
            count +=1
            temp = temp.next
        return count

    def search(self, data):
        temp = self.start
        while(temp):
            if data == temp.data:
                return temp 
            temp = temp.next

    def append(self , obj):
        new_node = Node()
        new_node.data = obj
        if self.start is None:
            self.start = new_node
            return
        
        current_node = self.start
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    def remove(self,index):
        if self.start is None:
            return
        current_node = self.start
        pos = 0 
        if pos == index:
            self.start = self.start.next
        else:
            while(current_node != None and pos +1 != index):
                pos += 1
                current_node = current_node.next
            
            if current_node != None:
                current_node.next = current_node.next.next

class Node:
    def __init__(self,value, right = None, left=None):
        self.right = right 
        self.left = left
        self.value = value
    
    def insert(self, value):
        if self.value is not None:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)

    def search(self, value):
         if self.value is not None:
            if value < self.value:
                if self.value == value:
                    return self
                if self.left is None:
                    return None
                return self.left.search(value)
            elif value > self.value:
                if self.value == value:
                    return self
                if self.left is None:
                    return None
                return self.right.search(value) 
        
class BinaryTree:
    def __init__(self):
        self.root =None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root.insert(value)

    def search(self, value):
        if self.root is None:
            return None
        if self.root.value == value:
            return self.root
        return self.root.search(value)
    
    def delete(self, value):
        search_node = self.search(value)
        if search_node is not None:
            search_node.value = None
        

    
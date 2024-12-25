class InfiniteRangeL:

    def __init__(self,start):
        self.start = start

    def __next__(self):
        self.start += 1
        return self.start
    
    def _iter_(self):
        return self
    
class Fibonachi:
    prev = 0
    current = 1
    index = None

    def __init__(self, index):
        self.index = index

    def __next__(self):
        if self.current+self.prev < self.index:
            next = self.current + self.prev
            self.prev = self.current
            self.current=next

            return self.current
        raise StopIteration
    
    def __iter__(self):
        return self

class Multiple:
    num = 0
    def __init__(self, mul):
        self.mul=mul

    def __next__(self):
        self.num += self.mul
        return self.num
    
    def __iter__(self):
        return self
        

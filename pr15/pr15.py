from io import TextIOWrapper

class List:
    __data: list[any] = []

    def __init__(self, *data: list[any]):
        self.__data = list(data)

    def __getitem__(self, index):
        if index > len(self.__data):
            return self.__data[-1]
        return self.__data[index]
    
    def __setitem__(self,index, value):
        if index > len(self.__data):
            self.__data[-1] = value
            return self.__data
        self.__data[index] = value
        return self.__data
    
    def _delitem__(self, index):
        if index > len(self.__data):
            del self.__data[-1]
        del self.__data[index]

class KeyValueStore:
    __data: dict = {}
    file:TextIOWrapper = None
    file_name = 'test/log.txt'
    def __init__(self, *data: dict, file_name = 'test/log.txt'):
        self.__data = dict(data)
        self.file=open(self.file_name,'w')

    def __del__(self):
        self.file.close()

    def __getitem__(self, index):
        return self.__data[index]
    
    def __setitem__(self, index, value):
        self.__data[index] = value
        self.file.write(self.__data)
        return self.__data
    
    def _delitem__(self,index):
        del self.__data[index]
        self.file.write(self.__data)


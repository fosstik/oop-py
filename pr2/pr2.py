from io import TextIOWrapper
import re

class UserSchem:
    ...

class DataBase:
    data = []
    def get_data(self, url): 
        with open(url, 'r', encoding='UTF-8') as f:
            result = f.readlines()
            f.close()
            self.serializers(result)
            return result

    def serializers(self, data:TextIOWrapper):
        content = []
        for i in data:
            schema = dict()
            line = [i for i in re.split(r'\s', i) if i != '']
            for index in range(0, len(line)-1, 2):
                schema[line[index]] = line[index+1]
            content.append(schema)
        self.create(content)
        return content
            
    def create(self, data):
        for i in data: 
            user = UserSchem()
            for key, item in i.items():
                setattr(user, key, item)
            self.data.append(user)

    def search(self, q):
        for user in self.data:
            for key, item in user.__dict__.items():
                if q in item:
                    return user


class Translator: 
    tr = {}

    def add(self, eng, rus):
        if self.tr.get(eng) is not None:
            if type(self.tr.get(eng)) is list:
                self.tr[eng].append(rus)
            else: 
             temp= self.tr[eng]
             self.tr[eng] = [temp, rus]
        else: 
            self.tr[eng] = rus

    def remove(self, eng):
        del self.tr[eng]

    def translate(self, eng):
        return self.tr[eng]
    
test = Translator()

test.add('car', 'машина')
test.add('car', 'транспорт')

print(test.translate('car'))



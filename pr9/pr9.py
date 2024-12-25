from typing import Any


class Handler:
    def __init__(self, methods=('GET')):
        self.methods = methods
    def get(self, func,req, *args, **kwargs):
        return func(req, *args, **kwargs)
    
    def post(self, func,req, *args, **kwargs):
        return func(req, *args, **kwargs)
    
    def __call__(self, func, *args, **kwargs):
        type_methods = {
            'GET':self.get,
            'POST':self.get,           
        }
        def wrapper(req, *args, **kwargs):
            if req['methods'] not in self.methods:
                raise f'Данная страница не принимает тип запросов {req['methods']}'
            return type_methods[req['methods']](func,req, *args, **kwargs)
        return wrapper
            
@Handler(methods=('POST'))
def get_page(req):
    return 'Hello world'
# print(
#     get_page({
#         'methods':'POST',
#     })
# )


class Power:
   def __init__(self, n):
       self.n = n

   def __call__(self, x):
       return x ** self.n

class Repeat:
    def __init__(self, n):
        self.n = n
    def __call__(self, func):
        def wrapper():
            for _ in range(self.n):
                func()
        return wrapper

@Repeat(5)
def test():
    print('test')

test()
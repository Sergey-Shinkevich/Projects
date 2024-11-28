import inspect
class introspection_info:
    def __init__(self, obj):
        self.obj = obj
        self.info()
    def  info(self):
        temp = str(type(self.obj))
        temp = temp.split()
        print(f'Класс:{temp[1]}')
        a = dir(self.obj)
        argument = []
        method = []
        for i in a:
            if i[0] == '_':
                argument.append(i)
            else:
                method.append(i)
        print(f'Аргументы: {argument}')
        print(f'Методы: {method}')
        temp = str(inspect.getmodule(self))
        temp = temp.split()
        print(f'Модуль: {temp[1]}')


introspection_info(42)

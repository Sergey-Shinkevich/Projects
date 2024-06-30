my_dict = {'Masha': 1980, 'Sasha': 1995, 'Ivan': 2000}
print('my_dict =', my_dict)
print('Existing value:', my_dict.get('Sasha'))
print('Not existing value:', my_dict.get('Sergey'))
my_dict.update({'Sergey': 2005, 'Anton': 2001})
print('Deleted value:', my_dict.pop('Masha'))
print('Modified dictionary:', my_dict)
# --------------------------------------------------
print('-------------------------------------------------------------------------------------')
my_set = {1, 2, 3, 4, 5, 'Sun', 1, 2, 3, 'Sun', 'Moon'}
print('Set:', my_set)
my_set.add(7)
my_set.add('Mars')
my_set.discard('Sun')
print('Modified set:', my_set)

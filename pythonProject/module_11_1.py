import numpy
test_array = numpy.array([1, 9, 3, 4, 5, 2, 4, 8, 2])
print(test_array)
print(type(test_array))
print(f'Количество элементов массива равно {test_array.size}')
print(f'Уникальные элементы массива: {numpy.unique(test_array)}')
print(f'Сортировка массива: {numpy.sort(test_array)}')


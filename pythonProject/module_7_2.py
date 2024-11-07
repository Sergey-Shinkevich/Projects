def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    dict_1 = {}
    for i in range(0, len(strings)):
        dict_1[(i+1, file.tell())] = strings[i]
        file.write(strings[i] + '\n')
    file.close()
    return dict_1


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
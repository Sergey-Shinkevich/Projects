first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']
temp = list(zip(first, second))
first_result = (len(temp[i][0]) - len(temp[i][1]) for i in range (len(temp)) if len(temp[i][0]) != len(temp[i][1]))
second_result = (len(first[i])  == len(second [i]) for i in range(len(first)))

print(list(first_result))
print(list(second_result))

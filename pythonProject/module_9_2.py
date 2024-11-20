first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

def first_result():
    first_result = [len(i) for i in first_strings if len(i) >= 5]
    return  list(first_result)

def second_result():
    second_result = [(i, j) for i in first_strings for j in second_strings if len(i) == len(j)]
    return list(second_result)

def  third_result():
    third_strings = first_strings + second_strings
    third_result = {i: len(i) for i in third_strings if len(i) % 2 == False}
    return third_result

print(first_result())
print(second_result())
print(third_result())
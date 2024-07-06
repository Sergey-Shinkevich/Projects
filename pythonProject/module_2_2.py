first = int(input('Введите First: '))
second = int(input('Введите Second: '))
third = int(input('Введите Third :'))
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)


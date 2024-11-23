def is_prime(function):
    def wrapper(a, b, c):
        result = function(a, b, c)
        count = 0
        for i in range(2, result):
            if result % i > 0:
                count += 1
        if count == result - 2:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)

result = sum_three(1, 3, 6)
print(result)

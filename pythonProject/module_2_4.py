numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1,len(numbers)):
    is_prime = True
    for j in range(2,i):
        if numbers[i]%j == 0:
            is_prime = False
    if is_prime == True:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])
print('Numbers=', numbers)
print('Primes', primes)
print('Not Primes', not_primes)

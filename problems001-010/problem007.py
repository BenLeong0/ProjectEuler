from math import sqrt

current_number = 2
primes = [2]
n = 10001

while len(primes) != n:
    current_number += 1
    prime = True
    for i in primes:
        if i > sqrt(current_number) + 1:
            break
        elif current_number % i == 0:
            prime = False
            break
    if prime is True:
        primes.append(current_number)


print(primes)
print(str(n) + 'th prime is ' + str(primes[-1]))

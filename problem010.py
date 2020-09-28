from math import sqrt

current_number = 2
primes = [2]
n = 2000000
current_sum = 2

while current_number < n:
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
        current_sum += current_number


print(current_sum)

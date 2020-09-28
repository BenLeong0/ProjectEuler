from math import sqrt

n = 10000
integers = [i+3 for i in range(n-3)]

def d(n):
    divisors = [1]
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(int(n/i))
    if sqrt(n) == int(sqrt(n)):
        divisors.append(int(sqrt(n)))
    return sum(divisors)

amicables = []

for i in integers:
    if i == d(d(i)) and i != d(i):
        print(i, 'and', d(i), 'are an amicable pair')
        amicables.append(i)
        amicables.append(d(i))
        integers.remove(d(i))

print('The sum of amicable numbers less that', n, 'is', sum(amicables))

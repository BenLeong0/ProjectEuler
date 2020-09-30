from math import sqrt


def get_proper_factors(n):
    divisors = []
    for i in range(1, 1 + int(sqrt(n))):
        if n % i == 0:
            divisors.append(i)
            if i != int(n/i):
                divisors.append(int(n/i))
    divisors.remove(n)
    return divisors


def is_prime(n):
    if n <= 0:
        return False
    elif len(get_proper_factors(n)) == 1:
        return True
    else:
        return False


print(is_prime(1))
print(is_prime(5))

ab = [0,0]
max_length = 0
for a in range(-999,1000):
    for b in range(-1000,1001):
        n = 0
        while is_prime(n**2 + a*n + b):
            n += 1
        if n > max_length:
            max_length = n
            ab = [a,b]

print(ab, ab[0]*ab[1])

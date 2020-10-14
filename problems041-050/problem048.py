from math import sqrt

powers = [0]


def cut_power(a, n):
    power = a ** n
    if len(str(power)) > 10:
        power = int(str(power)[-10:])
    return power


def cut_product(a,b):
    product = a * b
    if len(str(product)) > 10:
        product = int(str(product)[-10:])
    return product


def min_factors(n):
    i = 2
    while i < sqrt(n):
        if n % i == 0:
            return i, int(n/i)
        i += 1
    return n, 1


n = 1
while n <= 1000:
    a, b = min_factors(n)
    if b == 1:      # primes
        powers.append(cut_power(a,a))
    else:
        p = cut_product(cut_power(powers[a],b), cut_power(powers[b],a))
        powers.append(p)
    n += 1

cut_sum = str(sum(powers))[-10:]
while len(cut_sum) < 10:            # add zeroes in case cut off
    cut_sum = '0' + cut_sum
print(cut_sum)

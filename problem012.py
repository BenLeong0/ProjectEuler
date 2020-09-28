from math import sqrt


def find_factors(n):
    counter = 0
    factors = []
    while counter <= sqrt(n):
        counter += 1
        if counter == sqrt(n):
            factors.append(counter)
            break
        elif n % counter == 0:
            factors.append(counter)
            factors.append(int(n / counter))
    factors.sort()
    return factors


t = 0
i = 0

while i > -1:
    i += 1
    t += i
    if len(find_factors(t)) > 500:
        i = -10
        break

print(t)
print(len(find_factors(t)))

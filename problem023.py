from math import sqrt

# 1. find all abundant numbers
# 2. find all their sums
# 3. subtract from total sum


def get_proper_factors(n):
    divisors = []
    for i in range(1, 1 + int(sqrt(n))):
        if n % i == 0:
            divisors.append(i)
            if i != int(n/i):
                divisors.append(int(n/i))
    divisors.remove(n)
    return divisors


def is_abundant(n):
    divisors = get_proper_factors(n)
    return n < sum(divisors)


abundants = []
for i in range(28123):
    if is_abundant(i+1):
        abundants.append(i+1)

length = len(abundants)
sums = {}
for i in range(28123):
    sums[str(i+1)] = False

for a in range(length):
    if abundants[a] > 28123/2:
        break
    for b in range(a, length):
        sums[str(abundants[a] + abundants[b])] = True

sum = 0
for key in sums:
    if not sums[key]:
        sum += int(key)

print(sum)

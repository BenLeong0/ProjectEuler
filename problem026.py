from decimal import *
getcontext().prec = 5000

def remove_twos_and_fives(n):
    if n % 2 == 0:
        return remove_twos_and_fives(n/2)
    elif n % 5 == 0:
        return remove_twos_and_fives(n/5)
    else:
        return n


def cycle_length(n):
    denom = remove_twos_and_fives(n)
    if denom == 1:
        return 0
    i = 9
    while not int(Decimal(i) / Decimal(denom)) == Decimal(i) / Decimal(denom):
        i *= 10
        i += 9
    return len(str(i))

max_length = [0, 0]
for i in range(1,1000):
    print([i, cycle_length(i)])
    if cycle_length(i) > max_length[1]:
        max_length = [i, cycle_length(i)]

print(max_length)

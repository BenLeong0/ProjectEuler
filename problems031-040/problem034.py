from math import factorial

def factorial_sum(n):
    sum = 0
    for digit in str(n):
        sum += factorial(int(digit))
    if sum == n:
        return True
    return False


sols = []
total = 0
for n in range(3,1000000):
    if factorial_sum(n):
        sols.append(n)
        total += n

print(sols)
print(total)

import math

n = 100
# f = str(math.factorial(n))
def factorial_string(x):
    total = 1
    for i in range(x):
        total *= i+1
    return str(total)
f = factorial_string(n)
sum = 0

for number in f:
    sum += int(number)

print('The sum of the digits of', n, 'factorial is', sum)

# def power(a, n):
#     if n == 1:
#         return a
#     elif n % 2 == 0:
#         return power(a, int(n / 2)) ** 2
#     else:
#         return a * power(a, (n - 1) / 2) ** 2


p = 1000
total = 0


for i in str(2 ** p):
    total += int(i)

print(total)

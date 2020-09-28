from math import sqrt

# 1. find all abundant numbers
# 2. find all their sums
# 3. subtract from total sum

def abundant(n):
    divisors = [1]
    if n < 1:
        return False
    for i in range(2, int(sqrt(n)+1)):
        if n == i**2:
            divisors.append(int(sqrt(n)))
        elif n % i == 0:
            divisors.append(i)
            divisors.append(int(n/i))
    if sum(divisors) > n:
        return 'abun'
    if sum(divisors) == n:
        return 'perf'
    else:
        return False

abundants = []
perfects = []

for i in range(28123):
    if abundant(i) == 'abun':
        abundants.append(i)
    if abundant(i) == 'perf':
        perfects.append(i)

abundant_sums = []
print(len(abundants))

pos=0
for i in abundants:
    if i > 28123/2:
        break
    pos += 1

# for i in range(len(abundants)):
#     print('========\nNew start at', i, '!!\n===========')
#     m = abundants[i]
#     for j in abundants[i:]:
#         if m+j < 28123:
#             if abundant_sums.count(m+j) == 0:
#                 abundant_sums.append(m+j)
#                 print(i, m,j,m+j)
#         else:
#             print('BREAK')
#             break
#
# sum = int((28123*28122) / 2) - sum(abundant_sums)
#
# print(sum)
print(abundants)
print(perfects)

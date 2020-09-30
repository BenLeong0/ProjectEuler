results = []

for n in range(2,1000000):
    sum = 0
    for digit in str(n):
        sum += int(digit) ** 5
    if sum == n:
        results.append(n)

sum = 0
for i in results:
    sum += i

print(sum)

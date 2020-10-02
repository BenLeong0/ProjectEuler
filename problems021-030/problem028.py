n = 501

sum = 1
for i in range(2, n+1):
    print(i, sum)
    length = 2*i - 1
    sum += length ** 2 * 4 - 6*(length-1)

print(sum)

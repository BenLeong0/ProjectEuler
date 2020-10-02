d = 0
n = 0
limits = [1,10,100,1000,10000,100000,1000000]
factors = []


while limits:
    n += 1
    d += len(str(n))
    if d >= limits[0]:
        current_limit = limits.pop(0)
        factors.append(int(str(n)[current_limit-d-1]))

product = 1
for fact in factors:
    product *= fact

print(factors)
print(product)

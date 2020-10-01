counts = {}
for a in range(1, 334):
    for b in range(a, 500):
        for c in range(b, 1000):
            if a**2 + b**2 == c**2:
                p = str(a+b+c)
                print(p, a, b, c)
                if p in counts:
                    counts[p] += 1
                else:
                    counts[p] = 1

print(counts)

max = 0
for key, val in counts.items():
    if val > max:
        sol = key
        max = val

print(sol)

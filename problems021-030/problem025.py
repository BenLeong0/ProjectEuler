F = [1, 1]
i=2

while len(str(F[0])) != 1000:
    i += 1
    F = [F[0] + F[1], F[0]]

print(i)

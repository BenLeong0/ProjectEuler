solved = False

for a in range(334):
    for b in range(a, 500):
        c = 1000 - b - a
        if a**2 + b**2 == c**2:
            sol = [a, b, c]
            solved = True
            break
    if solved is True:
        break


print(sol)
print(sol[0] * sol[1] * sol[2])

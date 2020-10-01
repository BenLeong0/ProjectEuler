digits = {1,2,3,4,5,6,7,8,9}

def find_pandig(x):
    sol = ''
    n = 0
    while len(sol) < 9:
        n += 1
        sol += str(x*n)
    if len(sol) == 9 and n > 1:
        sol_digits = set()
        for digit in sol:
            sol_digits.add(int(digit))
        if sol_digits == digits:
            return int(sol)
    return 0


max = 0
for x in range(100000):
    if find_pandig(x) > max:
        print(x, find_pandig(x))
        max = find_pandig(x)

print(max)

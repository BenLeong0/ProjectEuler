solutions = {0}

digits = []
for i in range(1, 10):
    digits.append(str(i))

for i in range(9):
    for j in range(8):
        for k in range(7):
            for l in range(6):
                for m in range(5):
                    tempdigs = digits[:]
                    a = tempdigs.pop(i)
                    b = tempdigs.pop(j)
                    c = tempdigs.pop(k)
                    d = tempdigs.pop(l)
                    e = tempdigs.pop(m)
                    solint = int(a) * int(b+c+d+e)
                    prod = a+' * '+b+c+d+e
                    sol = str(solint)
                    if len(sol) != 4:
                        continue
                    letters = []
                    for letter in sol:
                        letters.append(letter)
                        letters.sort()
                        if letters == tempdigs:
                            print(prod, '=', sol)
                            solutions.add(solint)

for i in range(9):
    for j in range(8):
        for k in range(7):
            for l in range(6):
                for m in range(5):
                    tempdigs = digits[:]
                    a = tempdigs.pop(i)
                    b = tempdigs.pop(j)
                    c = tempdigs.pop(k)
                    d = tempdigs.pop(l)
                    e = tempdigs.pop(m)
                    solint = int(a+b) * int(c+d+e)
                    prod = a+b+' * '+c+d+e
                    sol = str(solint)
                    if len(sol) != 4:
                        continue
                    letters = []
                    for letter in sol:
                        letters.append(letter)
                        letters.sort()
                        if letters == tempdigs:
                            print(prod, '=', sol)
                            solutions.add(solint)

sum = 0
for solu in solutions:
    sum += solu

print(solutions)
print(sum)

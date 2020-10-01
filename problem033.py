import fractions

digits = []
for i in range(1, 10):
    digits.append(str(i))

count = 0

def fraction_a(a,b,c):
    num = int(a+b)
    den = int(c+a)
    if num > den:
        return False
    if num/den == int(b)/int(c):
        return True
    return False


def fraction_b(a,b,c):
    num = int(a+b)
    den = int(b+c)
    if num > den:
        return False
    if num/den == int(a)/int(c):
        return True
    return False


# NOT INCLUDING 0 FOR NOW

numerators = []
denominators = []

for i in range(9):
    for j in range(8):
        for k in range(7):
            tempdigs = digits[:]
            a = tempdigs.pop(i)
            b = tempdigs.pop(j)
            c = tempdigs.pop(k)
            if fraction_a(a,b,c):
                count += 1
                numerators.append(int(a+b))
                denominators.append(int(c+a))
                print(a+b, '/', c+a)
            if fraction_b(a,b,c):
                count += 1
                numerators.append(int(a+b))
                denominators.append(int(b+c))
                print(a+b, '/', b+c)

num = 1
den = 1

for i in range(4):
    num *= numerators[i]
    den *= denominators[i]

print(num, '/', den)
print(fractions.Fraction(num, den))

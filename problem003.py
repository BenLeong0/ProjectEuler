x = 600851475143


def factor(a):
    b = a.pop()
    for i in range(2, b + 1):
        if b == i:
            a.append(b)
            a.insert(0, 0)
            break
        elif b % i == 0:
            a.append(i)
            a.append(int(b / i))
            break
    return a


def all_factors(m):
    m = [m]
    while m[0] != 0:
        m = factor(m)
    del m[0]
    return m


y = all_factors(x)
print(y)
print("Primes factors are: " + str(y))
print("Largest prime factor is: " + str(y[-1]))

if __name__ == "__main__":
    import sys
    print(all_factors(int(sys.argv[1])))

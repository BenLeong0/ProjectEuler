def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


# left to right
def f(n):
    if isPrime(n):
        if len(str(n)) == 1:
            return True
        return f(int(str(n)[1:]))
    return False


# right to left
def g(n):
    if isPrime(n):
        if len(str(n)) == 1:
            return True
        return g(int(str(n)[:-1]))
    return False


count = 0
sum = 0
sols = []
n = 10

while count != 11:
    if f(n) and g(n):
        count += 1
        sum += n
        sols.append(n)
        print(n)
    n += 1

print(sum, sols)

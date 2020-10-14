def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def f(primes):
    for i in range(len(primes)):
        length = len(primes) - i
        for j in range(i):
            current = primes[j:j+length]
            total = sum(current)
            if total > n:
                break
            if isPrime(total):
                return [total, current]
    return primes


n = 1000000

primes = []
for i in range(int(n/2)):
    if isPrime(i): primes.append(i)

print(f(primes))

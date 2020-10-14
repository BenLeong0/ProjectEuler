saved_factors = [{},{},{2},{3},{4}]

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def prime_factors(n):
    i = 2
    while i != n:
        if n % i == 0:
            factors = {i}
            factors.update(saved_factors[int(n/i)])
            break
        i += 1
    return factors


def update_saved(n, streak):
    if isPrime(n):
        saved_factors.append({n})
        return 0
    else:
        factors = prime_factors(n)
        saved_factors.append(factors)
        if len(factors) == 4:
            streak += 1
        else:
            streak = 0
        return streak


streak = 0
n = 5

while True:
    streak = update_saved(n, streak)
    if streak == 4:
        print(n-3,n-2,n-1,n)
        break
    n += 1

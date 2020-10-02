"""
Can't be 8- or 9- pandigital, else it would be divisible by 3 and not prime
"""

all_digits = {1,2,3,4,5,6,7}
evens_and_five = {'0', '2', '4', '6', '5'}

def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def isPandigital(n):
    digits = set()
    for digit in str(n):
        digits.add(int(digit))
    if digits == all_digits:
        return True
    return False


n = 7654321
while True:
    if isPandigital(n) and str(n)[-1] not in evens_and_five:
        if isPrime(n):
            print(n, 'is pandigital AND prime!')
            break
        print(n, 'is pandigital, but not prime.')
    n -= 1

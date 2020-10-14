# Noticed that it must be the 4th digit that stays constant
checked = set()


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True


def get_permutations(n):
    perms = [n]
    perms.append(int(str(n)[1] + str(n)[2] + str(n)[0] + str(n)[3]))
    perms.append(int(str(n)[2] + str(n)[0] + str(n)[1] + str(n)[3]))
    perms.sort()
    return(perms)


for a in range(1, 10):
    for b in range(a, 10):
        for c in range(a, 10):
            for d in range(10):
                if a == b == c:
                    continue
                n = int(str(a) + str(b) + str(c) + str(d))
                if not isPrime(n):
                    continue
                perms = get_permutations(n)
                diff = (perms[2] - perms[1]) - (perms[1] - n)
                if isPrime(perms[1]) and isPrime(perms[2]) and diff == 0:
                    print(perms)

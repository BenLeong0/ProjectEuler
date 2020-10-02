def isPrime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

count = 0
for n in range(2, 1000000):
    n = str(n)
    rotations = set()
    for i in range(len(n)):
        rotation = n[i:]+n[:i]
        # print(n[i:]+n[:i])
        rotations.add(int(n[i:]+n[:i]))
    if all(isPrime(i) for i in rotations):
        print(rotations)
        count += 1

print(count)

# go through odd composite numbers, n
# generate squares up to n/2
# check if n - 2 * sq is prime

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

squares = [[1], 2]

n = 1
done = False
while not done:
    n += 1
    if isPrime(n) or n % 2 == 0:
        continue
    while squares[0][-1] < n / 2:
        squares[0].append(squares[1] ** 2)
        squares[1] += 1
    done = True
    for square in squares[0]:
        if isPrime(n - 2 * square):
            print(n, square, n - 2 * square)
            done = False
            break

print('Solution:',n)

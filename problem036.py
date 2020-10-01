def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

sum = 0
for n in range(1000000):
    if is_palindrome(n):
        binary = "{0:b}".format(n)
        if is_palindrome(binary):
            print(n, binary)
            sum += n

print(sum)

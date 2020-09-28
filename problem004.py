x = [0, 0, 0]
digits = 3


def palindrome(a):
    word = [digit for digit in str(a)]
    truth_value = True
    for n in range(int(len(word)/2)):
        if word[n] != word[-n-1]:
            truth_value = False
    return truth_value


for i in range(10**(digits-1), 10**digits):
    for j in range(i, 10**digits):
        if palindrome(i * j) is True and i*j > x[-1]:
            x = [i, j, i*j]

print(x)

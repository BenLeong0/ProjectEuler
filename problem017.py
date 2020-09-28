length = 0
letters = {'0': 0, '1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5, '9': 4,
           '10': 3, '11': 6, '12': 6, '13': 8, '14': 8, '15': 7, '16': 7, '17': 9, '18': 8, '19': 8,
           '20': 6, '30': 6, '40': 5, '50': 5, '60': 5, '70': 7, '80': 6, '90': 6}


def two_digit_length(m, n):
    if m == 0:
        return letters[str(n)]
    if m == 1:
        return letters[str(m) + str(n)]
    else:
        return letters[str(m) + '0'] + letters[str(n)]


for a in range(10):
    for b in range(10):
        for c in range(10):
            if a == 0 and b == 0 and c == 0:
                pass
            if a != 0:
                length += letters[str(a)] + 7         # 'a hundred'
                if b != 0 or c != 0:
                    length += 3         # 'and'
            length += two_digit_length(b, c)
            print([str(a) + str(b) + str(c), length])


length += 11    # for 'one thousand

print(two_digit_length(0, 4))
print(length)

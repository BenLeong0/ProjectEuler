# Create list of digits
digits = []
for i in range(10):
  digits.append(i)

# Starts with 0, then 01, then 012, and uses previous result as permutations
# to arrange the following numbers
perms = [[0]]
for digit in digits[1:]:
    temp_perms = []
    range = digits[:digit+1]
    for i in range:
        remains = range[:]
        remains.remove(i)
        for perm in perms:
            temp_perm = [i]
            for pos in perm:
                # print(remains, perm, pos)
                temp_perm.append(remains[pos])
            temp_perms.append(temp_perm)
    perms = temp_perms

print(perms[1000000-1])

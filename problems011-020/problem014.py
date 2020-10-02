def collatz(k):
    if k % 2 == 0:
        m = int(k / 2)
        return m
    else:
        m = 3 * k + 1
        return m


lengths = {'1': 1}
max_value = 1
max_length = 1

upper_bound = 10 ** 6


for i in range(int(upper_bound / 2), upper_bound):
    x = [i]
    while True:
        c = collatz(x[-1])
        if str(c) in lengths:
            for j in range(len(x)):
                lengths[str(x[j])] = lengths[str(c)] + len(x) - j
            if lengths[str(i)] > max_length:
                max_length = lengths[str(i)]
                max_value = i
            # print([max_value, max_length])
            break
        else:
            x.append(c)

print('The number with the longest Collatz chain less than ' + str(upper_bound) + ' is ' +
      str(max_value) + ', with a chain of length ' + str(max_length) + '.')

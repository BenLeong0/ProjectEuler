'''
Compute all combinations for sums less than £20, using all coins EXCEPT 1p.
The difference between the sum and £2 can be filled in with all 1p coins.
eg: £1 with two 50p coins ~~ £2 with two 50p coins and one hundred 1p coins.
The solution is just the number of these combinations, plus one for 200 x 1p.
'''

coins = [2,5,10,20,50,100,200]

methods = [[]]

for n in range(1,201):
    print('NEW:', n)
    current_methods = []
    for coin in coins:
        if coin == n:
            current_methods.append([coin])
        elif coin < n:
            for method in methods[n-coin]:
                new_meth = method[:]
                new_meth.append(coin)
                new_meth.sort()
                if new_meth not in current_methods:
                    current_methods.append(new_meth)
    methods.append(current_methods)

print(len(methods[-1]))

sum = 1     # 200 1p coins

for method in methods:
    print(method)
    sum += len(method)

print(sum)

x = 0
y = 0
h = 100

for i in range(h + 1):
    x += i ** 2
    y += i

y = y ** 2
print(y - x)

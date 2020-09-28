n = 20
m = [[1] * (n+1)]


for i in range(n):
    row = [1]
    for j in range(n):
        row.append(0)
    m.append(row)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        m[i][j] = m[j][i] = m[i-1][j] + m[i][j-1]


print(m)
print('In an ' + str(n) + 'x' + str(n) + ' grid there are ' + str(m[n][n]) + ' different routes.')

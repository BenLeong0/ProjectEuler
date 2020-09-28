from problem065values import *

# val = [[3],
#        [7, 4],
#        [2, 4, 6],
#        [8, 5, 9, 3]
#        ]

i = 2

ans = val[0]

for i in range(1, len(val)):
    current_ans = [val[i][0] + ans[0]]
    for j in range(1, i):
        current_ans.append(val[i][j] + max(ans[j-1], ans[j]))
    current_ans.append(val[i][i] + ans[i-1])
    ans = current_ans

print('The max total is:', max(ans))

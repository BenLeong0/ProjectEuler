solutions = {0}

def function(n):
    if int(n[1:4]) % 2 == 0:
        if int(n[2:5]) % 3 == 0:
            if int(n[3:6]) % 5 == 0:
                if int(n[4:7]) % 7 == 0:
                    if int(n[5:8]) % 11 == 0:
                        if int(n[6:9]) % 13 == 0:
                            if int(n[7:10]) % 17 == 0:
                                return True
    return False


sols = []

digits = []
for i in range(10):
    digits.append(str(i))

for d in [0,2,4,6,8]:
    for a in range(9):
        for b in range(8):
            for c in range(7):
                for e in range(6):
                    for f in range(5):
                        for g in range(4):
                            for h in range(3):
                                for i in range(2):
                                    for j in range(1):
                                        tempdigs = digits[:]
                                        n = tempdigs.pop(d)
                                        for x in [a,b,c]:
                                            n = tempdigs.pop(x) + n
                                        for x in [e,f,g,h,i,j]:
                                            n += tempdigs.pop(x)
                                        if function(n):
                                            sols.append(int(n))
                                            print(n)

print(sols)
print(sum(sols))

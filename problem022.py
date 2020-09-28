import string

with open('problem022names.txt', 'r') as f:
    a = f.readline()

scores = {}
for i in range(len(list(string.ascii_uppercase))):
    scores[list(string.ascii_uppercase)[i]] = i + 1


def names_score(name, x):
    score = 0
    for i in range(len(name)):
        score += scores[name[i]]
    return score * x


names = []
a = a[1:]
print(a)

while a.count('"') > 0:
    index = a.index('"')
    names.append(a[:index])
    a = a[index+3:]

names.sort()

total = 0

for i in range(len(names)):
    total += names_score(names[i], i+1)

print(total)
print(names_score('COLIN', 938))

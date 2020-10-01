import string

triangles = set()
n = 1
while True:
    t = int(n*(n+1)/2)
    if t > 192:
        break
    triangles.add(t)
    n += 1


with open('problem042words.txt', 'r') as f:
    a = f.readline()

scores = {}
for i in range(len(list(string.ascii_uppercase))):
    scores[list(string.ascii_uppercase)[i]] = i + 1


def score(name):
    score = 0
    for i in range(len(name)):
        score += scores[name[i]]
    return score


words = []
a = a[1:]

while a.count('"') > 0:
    index = a.index('"')
    words.append(a[:index])
    a = a[index+3:]

count = 0
for word in words:
    if score(word) in triangles:
        count += 1

print(count)

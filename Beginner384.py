from itertools import combinations

s = list(map(int, input().split()))
coms = []
n = 5
while n > 0:
    for c in combinations([0, 1, 2, 3, 4], n):
        coms.append(c)
    n -= 1

scores = []
for c in coms:
    total = 0
    name = ""
    for i in c:
        total += s[i]
        name += chr(65+i)
    scores.append((total, name))
scores.sort(key=lambda x: (-x[0], x[1]))
for i in range(len(scores)):
    print(scores[i][1])

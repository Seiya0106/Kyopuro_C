from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(list)
for i, a in enumerate(A):
    d[a].append(i)

for key in sorted(d, reverse=True):
    if len(d[key]) == 1:
        print(d[key][0] + 1)
        exit()
print(-1)

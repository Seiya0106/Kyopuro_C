from collections import Counter
from itertools import combinations

n, k = map(int,input().split())
S = []
for _ in range(n):
    s = input()
    S.append(Counter(s))

ans = 0
cnt = 0
all2 = True
for i in range(1, n+1):
    for c in combinations(S, i):
        V = Counter()
        for v in c:
            V += v
        for va in V.values():
            if va == k:
                cnt += 1
        ans = max(ans, cnt)
        cnt = 0
print(ans)

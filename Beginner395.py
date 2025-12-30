n = int(input())
A = list(map(int, input().split()))

pairs = []
for i, a in enumerate(A):
    pairs.append((a, i))
pairs.sort()

ans = n
ok = False
for i in range(n-1):
    if pairs[i][0] == pairs[i+1][0]:
        ok = True
        ans = min(ans, pairs[i+1][1] - pairs[i][1] + 1)

if ok:
    print(ans)
else:
    print(-1)

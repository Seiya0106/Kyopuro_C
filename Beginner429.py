from collections import Counter

N = int(input())
A = list(map(int, input().split()))
count = Counter(A)

ans = 0
for a in count:
    ans += (count[a] * (count[a] - 1) // 2 * (N - count[a]))
print(ans)

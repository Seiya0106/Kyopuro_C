n = int(input())
A = list(map(int,input().split()))
for i in range(n):
    A[i] -= 1

same = 0
for i, a in enumerate(A):
    if i == a:
        same += 1

ans = same * (same - 1) // 2
for i, j in enumerate(A):
    if i < j and A[j] == i:
        ans += 1
print(ans)

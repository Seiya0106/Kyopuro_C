n, k = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
remain = n - k
min_dif = float("inf")
for i in range(k+1):
    dif = A[remain + i - 1] - A[i]
    min_dif = min(min_dif, dif)
print(min_dif)

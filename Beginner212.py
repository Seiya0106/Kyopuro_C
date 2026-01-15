n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

i = 0
j = 0
min_dif = float("inf")

while i < n and j < m:
    dif = abs(A[i] - B[j])
    min_dif = min(min_dif, dif)
    if A[i] < B[j]:
        i += 1
    else:
        j += 1
print(min_dif)

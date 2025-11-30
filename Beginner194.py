N = int(input())
A = list(map(int, input().split()))

a1 = 0
for i in range(N):
    a1 += A[i] ** 2
a1 = a1 * N

a2 = 0
for j in range(N):
    a2 += A[j]
a2 = a2 ** 2

print(a1 - a2)

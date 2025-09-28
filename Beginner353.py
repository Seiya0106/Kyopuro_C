N = int(input())
A = list(map(int, input().split()))
R = [0] * (N + 1)
result = 0
for i in range(N - 1):
    total = (A[i]) % 100000000
    result += total
print(result * (N - 1))

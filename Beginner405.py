N = int(input())
A = list(map(int, input().split()))

sum = 0
square_sum = 0
for i in range(N):
    sum += A[i]
    square_sum += A[i] * A[i]

print((sum * sum - square_sum) // 2)

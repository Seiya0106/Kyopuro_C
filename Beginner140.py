N = int(input())
B = list(map(int, input().split()))
A = [B[0]]
for i in range(N - 2):
    if B[i] > B[i + 1]:
        A.append(B[i + 1])
    else:
        A.append(B[i])
A.append(B[N - 2])
print(sum(A))

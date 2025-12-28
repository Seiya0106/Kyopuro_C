n = int(input())
A = list(map(int, input().split()))
W = []
for i in range(n):
    W.append(A[i])
    while True:
        if len(W) == 1:
            break
        elif W[-1] == W[-2]:
            w1= W[-1]
            for _ in range(2):
                W.pop()
            W.append(w1 + 1)
        else:
            break

print(len(W))

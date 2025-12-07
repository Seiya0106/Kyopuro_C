n = int(input())
A = list(map(int, input().split()))

domino = A[0]
for i, a in enumerate(A):
    if domino >= i + 1:
        domino = max(domino, i + A[i])
    else:
        break
if domino >= n:
    print(n)
else:
    print(domino)

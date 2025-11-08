N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))

H.sort()
B.sort()

ok = True
for i in range(K):
    if H[i] <= B[M - K + i]:
        continue
    else:
        ok = False
        break

if ok:
    print("Yes")
else:
    print("No")

N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))

H.sort()
B.sort(reverse=True)
hk = []
bk = []
for i in range(K):
    hk.append(H[i])
    bk.append(B[i])
bk.sort()
ok = True
for i in range(K):
    if hk[i] <= bk[i]:
        continue
    else:
        ok = False
        break

if ok:
    print("Yes")
else:
    print("No")

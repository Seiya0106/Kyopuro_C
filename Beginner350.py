N = int(input())
A = list(map(int, input().split()))
pos = [0] * (N + 1)
for i in range(N):
    pos[A[i]] = i

ope = []
issorted = False
for i in range(N):
    if A[i] != i + 1:
        issorted = True
        j = pos[i + 1]
        A[i], A[j] = A[j], A[i]
        ope.append((i + 1, j + 1))
        # 対応表も更新
        pos[A[j]] = j
        pos[A[i]] = i
if issorted:
    print(len(ope))
    for o in ope:
        print(o[0], o[1])
else:
    print(0)

t = int(input())

for _ in range(t):
    n = int(input())
    P = [0]
    A = []
    for i in range(n):
        w, p = map(int, input().split())
        P.append(P[i] + p)
        A.append(w + p)
    A.sort()
    s = 0
    cnt = 0
    for x in A:
        if s + x <= P[-1]:
            s += x
            cnt += 1
        else:
            break
    print(cnt)

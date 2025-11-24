from collections import deque

q = int(input())
dq = deque()
result = []
for _ in range(q):
    qry = list(map(int, input().split()))
    if qry[0] == 1:
        c, x = qry[1], qry[2]
        dq.append((x, c))
    else:
        k = qry[1]
        total = 0
        while k > 0:
            x, cnt = dq[0]
            if cnt <= k:
                total += x * cnt
                k -= cnt
                dq.popleft()
            else:
                total += x * k
                dq[0] = (x, cnt - k)
                k = 0
        result.append(total)
for r in result:
    print(r)

n = int(input())
doukasen = []
t = 0
for _ in range(n):
    a, b = map(int,input().split())
    doukasen.append((a, b))
    t += a / b
t /= 2
ans = 0
for d in doukasen:
    if t >= d[0] / d[1]:
        ans += d[0]
        t -= d[0] / d[1]
    else:
        ans += d[1] * t
        t -= t
print(ans)

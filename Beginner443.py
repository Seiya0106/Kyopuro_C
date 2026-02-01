n, t = map(int,input().split())
A = list(map(int,input().split()))
time = 0
d = 0
if n == 0:
    print(t)
    exit()
for a in A:
    if a - d < 0:
        continue
    time += min(a, a - d)
    d = a + 100
time += max(t - d, 0)
print(time)

n, t = map(int, input().split())
A = list(map(int, input().split()))

time = 0
next_open = 0

if n == 0:
    print(t)
    exit()

for a in A:
    if a < next_open:
        continue
    time += a - next_open
    next_open = a + 100

time += max(t - next_open, 0)
print(time)

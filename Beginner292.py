n = int(input())
ans = 0

for i in range(1, n):
    x = i
    y = n - i

    dx = 0
    j = 1
    while j * j <= x:
        if x % j == 0:
            dx += 1
            if x != j * j:
                dx += 1
        j += 1

    dy = 0
    j = 1
    while j * j <= y:
        if y % j == 0:
            dy += 1
            if y != j * j:
                dy += 1
        j += 1

    ans += dx * dy

print(ans)

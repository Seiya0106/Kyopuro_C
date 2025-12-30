n, m = map(int, input().split())
trout = set()
knight = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    trout.add((a, b))
    for dx, dy in knight:
        if 0 <= a + dx < n and 0 <= b + dy < n:
            trout.add((a+dx, b+dy))
print(n * n - len(trout))

n, m = map(int, input().split())
trout = set()
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    trout.add((a, b))
    if 0 <= a + 2 < n and 0 <= b + 1 < n:
        trout.add((a+2, b+1))
    if 0 <= a + 1 < n and 0 <= b + 2 < n:
        trout.add((a+1, b+2))
    if 0 <= a - 1 < n and 0 <= b + 2 < n:
        trout.add((a-1, b+2))
    if 0 <= a - 2 < n and 0 <= b + 1 < n:
        trout.add((a-2, b+1))
    if 0 <= a - 2 < n and 0 <= b - 1 < n:
        trout.add((a-2, b-1))
    if 0 <= a - 1 < n and 0 <= b - 2 < n:
        trout.add((a-1, b-2))
    if 0 <= a + 1 < n and 0 <= b - 2 < n:
        trout.add((a+1, b-2))
    if 0 <= a + 2 < n and 0 <= b - 1 < n:
        trout.add((a+2, b-1))
print(n * n - len(trout))

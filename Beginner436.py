n, m = map(int, input().split())
pos = set()
cnt = 0
for _ in range(m):
    r, c = map(int, input().split())
    if (r-1, c-1) in pos or (r-1, c) in pos or (r, c-1) in pos or (r, c) in pos:
        continue
    else:
        pos.add((r-1, c-1))
        pos.add((r-1, c))
        pos.add((r, c-1))
        pos.add((r, c))
        cnt += 1
print(cnt)

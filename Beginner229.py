n, w = map(int, input().split())
cheese = []
for _ in range(n):
    a, b = map(int, input().split())
    cheese.append((a, b))
cheese.sort(reverse=True)
totalB = 0
deli = 0
for i in range(n):
    if totalB + cheese[i][1] < w:
        if totalB <= w:
            deli += cheese[i][0] * cheese[i][1]
            totalB += cheese[i][1]
    else:
        deli += cheese[i][0] * (w - totalB)
        break
print(deli)

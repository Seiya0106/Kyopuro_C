n = int(input())
cnt = {}
for x in range(1, int(pow(n, 0.5))+1):
    for y in range(x+1, int(pow(n, 0.5))+1):
        total = x ** 2 + y ** 2
        if total <= n and total in cnt:
            cnt[total] += 1
        elif total <= n:
            cnt[total] = 1
ans = [k for k, v in cnt.items() if v == 1]
ans.sort()
print(len(ans))
print(*ans)

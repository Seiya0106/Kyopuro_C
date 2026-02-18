n = int(input())
H = list(map(int,input().split()))
ans = 1
for i in range(n):
    for d in range(1, n):
        cnt = 1
        for j in range(d, n-i, d):
            if H[i] != H[i+j]:
                break
            else:
                cnt += 1
        ans = max(ans, cnt)
print(ans)

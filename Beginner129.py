n, m = map(int,input().split())
ng = [False] * (n + 10)
dp = [0] * (n + 10)
MOD = 1000000007

for _ in range(m):
    a = int(input())
    ng[a] = True
dp[0] = 1
for i in range(n):
    for d in range(1, 3):
        if not ng[i+d]:
            dp[i+d] = (dp[i+d] + dp[i]) % MOD

print(dp[n])

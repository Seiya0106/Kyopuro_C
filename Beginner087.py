n = int(input())
pos = []
for _ in range(2):
    pos.append(list(map(int, input().split())))

dp = [[0] * n for _ in range(2)]
dp[0][0] = pos[0][0]

# 1行目（右に進むだけ）
for i in range(1, n):
    dp[0][i] = dp[0][i - 1] + pos[0][i]

# 2行目
dp[1][0] = dp[0][0] + pos[1][0]
for i in range(1, n):
    dp[1][i] = max(dp[0][i] + pos[1][i], dp[1][i - 1] + pos[1][i])

print(dp[1][n - 1])

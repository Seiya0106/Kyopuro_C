n = int(input())
LR = []
total_l = 0
total_r = 0
for _ in range(n):
    l, r = map(int, input().split())
    LR.append((l, r))
    total_l += l
    total_r += r
if total_l <= 0 and total_r >= 0:
    print("Yes")
    X = [LR[i][0] for i in range(n)]
    current_sum = sum(X)
    if current_sum == 0:
        print(*X)
        exit()
    else:
        for i in range(n):
            d = min(LR[i][1] - LR[i][0], -current_sum)
            current_sum += d
            X[i] += d
    print(*X)
else:
    print("No")

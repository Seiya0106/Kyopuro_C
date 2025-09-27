N, K = map(int, input().split())
day = 1
total = 0
# N行分のペアを受け取る
pairs = []
for _ in range(N):
    a, b = map(int, input().split())
    pairs.append((a, b))
pairs.sort(reverse=True)
for nums in pairs:
    total += nums[1]
    if total > K:
        day = nums[0]
        print(day + 1)
        exit()
print(1)

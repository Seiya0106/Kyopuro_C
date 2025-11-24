from collections import Counter

n = int(input())
a = list(map(int, input().split()))
nums = Counter(a)
# 全て1の場合は条件を満たさない
if all(n == 1 for n in nums.values()):
    print(-1)
    exit()
else:
    com = []
    length = 2 * (10 ** 5)
    # 数字とインデックスを保持
    for i, num in enumerate(a):
        com.append((num, i))
    com.sort()
    for j in range(n - 1):
        # 同じ数字かどうか判定し、距離を計算
        if com[j][0] == com[j + 1][0]:
            length = min(length, com[j+1][1] - com[j][1] + 1)
print(length)

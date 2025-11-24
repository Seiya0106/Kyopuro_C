from collections import Counter

n = int(input())
a = list(map(int, input().split()))
nums = Counter(a)
if all(n == 1 for n in nums.values()):
    print(-1)
    exit()
else:
    com = []
    length = 2 * (10 ** 5)
    for i, num in enumerate(a):
        com.append((num, i))
    com.sort()
    for j in range(n - 1):
        if com[j][0] == com[j + 1][0]:
            length = min(length, com[j+1][1] - com[j][1] + 1)
print(length)

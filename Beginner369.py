# AI生成
n = int(input())
a = list(map(int, input().split()))

total = n + (n - 1)
length = 2
for i in range(2, n):
    if a[i] - a[i - 1] == a[i - 1] - a[i - 2]:
        length += 1
        total += length - 2
    else:
        length = 2
print(total)

n, m = map(int,input().split())
nums = [0 for _ in range(n+1)]
for _ in range(m):
    a, b = map(int,input().split())
    nums[a] += 1
    nums[b] += 1

for i in range(1,n+1):
    num = n - nums[i] - 1
    if num <= 2:
        print(0, end=" ")
    else:
        ans = num * (num - 1) * (num - 2) // 6
        print(ans, end=" ")
print()

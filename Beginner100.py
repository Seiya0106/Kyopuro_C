N = int(input())
a = list(map(int, input().split()))
count = 0

for num in a:
    while num % 2 == 0:
        count += 1
        num /= 2
print(count)

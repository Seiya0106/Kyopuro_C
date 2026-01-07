s = input()
n = len(s)

total = 0

for i in range(n-1, -1, -1):
    v = int(s[i])
    if i < n-1:
        u = int(s[i+1])
    else:
        u = 0
    b = (10 + v - u) % 10
    total += b

ans = total + n
print(ans)

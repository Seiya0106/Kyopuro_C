n = int(input())
res = round(n ** (1 / 3))
for i in range(res, 0, -1):
    if i ** 3 <= n:
        s = str(i ** 3)
        m = len(s) // 2
        if len(s) % 2 != 0 and s[:m] == s[len(s):m:-1]:
            print(s)
            exit()
        elif s[:m] == s[len(s):m-1:-1]:
            print(s)
            exit()

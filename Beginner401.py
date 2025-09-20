def add(k, n):
    s = sum(a)
    mod = 10 ** 9
    for i in range(k, n + 1):
        a.append(s % mod)
        s += (a[i] - a[i - k]) % mod
    return a[n]

n, k = map(int, input().split())
a = [1] * k
print(add(k, n))

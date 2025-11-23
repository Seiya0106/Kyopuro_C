from itertools import groupby

s = input()
# ランレングス圧縮
a = [(v, len(list(x))) for v, x in groupby(s)]
# print(a)

ans = 0
for i in range(len(a) - 1):
    if int(a[i][0]) + 1 == int(a[i + 1][0]):
        ans += min(a[i][1], a[i + 1][1])
print(ans)

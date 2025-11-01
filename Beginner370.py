s = input()
t = input()
ans = []
n = len(s)

while s != t:
    nxt = "z" * n
    for i in range(n):
        if s[i] != t[i]:
            tmp = list(s)
            tmp[i] = t[i]
            tmp_str = "".join(tmp)
            # 辞書順最小
            nxt = min(nxt, tmp_str)
    ans.append(nxt)
    s = nxt

print(len(ans))
for e in ans:
    print(e)

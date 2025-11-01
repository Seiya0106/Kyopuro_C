N = int(input())
F, S = [], []
maxS, choice = 0, -1
for i in range(N):
    f, s = map(int, input().split())
    # 美味しさが一番大きいカップのインデックス
    if s > maxS:
        maxS = s
        choice = i
    
    F.append(f)
    S.append(s)

# 満足度計算
ans = 0
for i in range(N):
    if i != choice:
        t = maxS + S[i] // (2 if F[i] == F[choice] else 1)
        ans = max(ans, t)
print(ans)

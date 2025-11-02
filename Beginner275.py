from itertools import combinations

S = []
for _ in range(9):
    S.append(list(input()))

pone = []
# ポーンがある位置
for i in range(9):
    for j in range(9):
        if S[i][j] == "#":
            pone.append((i + 1, j + 1))

cnt = 0
for c in combinations(pone, 4):
    # 4点のペアの距離（2乗）をすべて計算
    dists = []
    for i in range(4):
        for j in range(i+1, 4):
            dists.append((c[i][0] - c[j][0]) ** 2 + (c[i][1] - c[j][1]) ** 2)
    dists.sort()
    # 辺長4本同じ、対角線2本同じ、辺長0以外
    if dists[0] > 0 and dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5]:
        cnt += 1

print(cnt)

# AI生成

# 入力を読み込む
N, K = map(int, input().split())

# K個の空のリストを作成
b = [[] for _ in range(K)]

# N個の整数を読み込む
a = list(map(int, input().split()))

# 各要素を b[i%K] に追加
for i in range(N):
    b[i % K].append(a[i])

# b の各リストを降順にソート
for i in range(K):
    b[i].sort(reverse=True)

# a を昇順にソート
a.sort()

# na を構築
na = []
for i in range(N):
    na.append(b[i % K][-1])  # 最後の要素を取得
    b[i % K].pop()            # 最後の要素を削除

# 比較
if a == na:
    print("Yes")
else:
    print("No")

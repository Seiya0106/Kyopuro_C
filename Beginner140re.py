# 入力の読み取り
N = int(input())
B = list(map(int, input().split()))

# A の初期化
A = [B[0]]  # 最初の要素を B[0] に設定

# A の要素を決定
for i in range(N - 2):
    # 現在の B[i] と次の B[i + 1] の最小値を A に追加
    A.append(min(B[i], B[i + 1]))

# 最後の要素を追加
A.append(B[-1])

# A の総和を計算して出力
print(sum(A))

# AI生成
import math
from itertools import permutations

N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

ord_list = list(range(N))

sm = 0
# 組み合わせを見つけ、それに合った距離を求める
for ord in permutations(ord_list):
    for i in range(N - 1):
        a = ord[i]
        b = ord[i + 1]

        dx = X[a] - X[b]
        dy = Y[a] - Y[b]

        sm += math.sqrt(dx * dx + dy * dy)

# 組み合わせの数だけわる
for i in range(N):
    sm /= (i + 1)

# 小数点以下10桁まで表示
print(f"{sm:.10f}")

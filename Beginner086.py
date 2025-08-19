# AI生成
N = int(input())
current_time, current_x, current_y = 0, 0, 0
is_possible = True

for _ in range(N):
    t, x, y = map(int, input().split())
    # 移動に関する差分を計算
    delta_t = t - current_time
    delta_x = abs(x - current_x)
    delta_y = abs(y - current_y)

    # 条件をチェック
    if delta_x + delta_y > delta_t or (delta_t - (delta_x + delta_y)) % 2 != 0:
        is_possible = False
        break

    # 現在の状態を更新
    current_time, current_x, current_y = t, x, y

# 結果を出力
if is_possible:
    print("Yes")
else:
    print("No")

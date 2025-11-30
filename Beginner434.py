T = int(input())

for i in range(T):
    N, H = map(int, input().split())
    prev_t = 0
    min_h = H
    max_h = H
    possible = True
    for j in range(N):
        t, l, u = map(int, input().split())
        # 移動できる時間
        dt = t - prev_t
        # いける範囲
        min_h -= dt
        max_h += dt
        # 可能な範囲
        min_h = max(min_h, l)
        max_h = min(max_h, u)
        # 条件を満たさない場合
        if min_h > max_h:
            possible = False
        # 時間の更新
        prev_t = t

    if possible:
        print("Yes")
    else:
        print("No")

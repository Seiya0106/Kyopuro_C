# AI生成
import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

left = 1
right = 10**9 + 1  # Xの探索範囲（制約より）

while left < right:
    mid = (left + right) // 2  # 真ん中の値を試す
    sell_cnt = bisect.bisect_right(A, mid)  # A[i] ≤ mid の人数
    buy_cnt = M - bisect.bisect_left(B, mid)  # B[i] ≥ mid の人数
    print(sell_cnt)
    print(buy_cnt)
    if sell_cnt >= buy_cnt:
        # 条件を満たすXがmid以下にもあるかもしれないので、右端を更新
        right = mid
    else:
        # 条件を満たすXはmidより大きいので、左端を更新
        left = mid + 1

print(left)

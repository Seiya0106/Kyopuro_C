from collections import deque

t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    eggs = deque()
    for i in range(n):
        day = i + 1
        # 朝：卵を仕入れる
        eggs.append([day, a[i]])
        # 昼：卵を使用する
        remaining = b[i]
        while remaining > 0:
            if eggs[0][1] <= remaining:
                remaining -= eggs[0][1]
                eggs.popleft()
            else:
                eggs[0][1] -= remaining
                remaining = 0
        # 夜：D日間以上経過した卵を処分
        cut_day = day - d
        while eggs and eggs[0][0] <= cut_day:
            eggs.popleft()
    total = sum(cnt for day, cnt in eggs)
    print(total)

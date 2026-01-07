n, q = map(int,input().split())
s = list(input())
shift = 0   # 回転によって元の位置からどれだけ動いたかを記録
for i in range(q):
    t, x = map(int,input().split())
    if t == 1:
        shift = (shift + x) % n
    elif t == 2:
        actual_index = (x - 1 - shift) % n
        print(s[actual_index])

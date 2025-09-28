# AI生成
def calc(level, is_red, X, Y):
    if level == 1:
        return 0 if is_red else 1
    if is_red:
        return calc(level - 1, True, X, Y) + calc(level, False, X, Y) * X
    else:
        return calc(level - 1, True, X, Y) + calc(level - 1, False, X, Y) * Y

N, X, Y = map(int, input().split())
print(calc(N, True, X, Y))

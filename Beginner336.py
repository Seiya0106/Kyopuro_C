# AI生成
N = int(input())

digits = [0, 2, 4, 6, 8]

def nth_good_integer(N):
    N -= 1  # 0始まりにする
    if N == 0:
        return "0"
    res = []
    while N > 0:
        res.append(str(digits[N % 5]))
        N //= 5
    return ''.join(res[::-1])

print(nth_good_integer(N))

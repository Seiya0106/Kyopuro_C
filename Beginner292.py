import sys

def solve():
    # 標準入力からの読み込み
    input = sys.stdin.read
    data = input().split()
    if not data:
        return
    
    N = int(data[0])
    
    # 約数の個数を前計算するための配列
    # d[i] は整数 i の約数の個数
    d = [0] * (N + 1)
    
    # 1 から N までの数について約数の個数をカウント
    # 調和級数の和により計算量は O(N log N)
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            d[j] += 1
            
    ans = 0
    # AB = x, CD = N - x となる x を全探索
    # 1 <= x <= N - 1
    for x in range(1, N):
        y = N - x
        # (A,B)の組み合わせ数 * (C,D)の組み合わせ数
        ans += d[x] * d[y]
        
    print(ans)

if __name__ == '__main__':
    solve()

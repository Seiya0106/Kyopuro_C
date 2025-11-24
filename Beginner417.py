# AI生成
from collections import defaultdict

def main():
    # N を読み込む（空行などを避けるため strip()）
    N = int(input().strip())

    # A を N 個読み込む（複数行に分かれていても対応）
    A = []
    while len(A) < N:
        A.extend(map(int, input().split()))

    # counter[key] は「ある j に対して j + A[j] == key となる j の個数」
    counter = defaultdict(int)
    ans = 0

    for i, a in enumerate(A):
        ans += counter[i - a]   # 過去の j で j + A[j] == i - A[i] の個数を加算
        counter[i + a] += 1     # 今の i の j + A[j] を登録

    print(ans)

if __name__ == "__main__":
    main()

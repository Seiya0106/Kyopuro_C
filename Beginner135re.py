# AI生成
def max_monsters_defeated(N, A, B):
    ans = 0  # 倒したモンスターの総数

    for i in range(N):
        # 勇者 i が街 i のモンスターを倒す
        defeated_in_current_city = min(A[i], B[i])
        ans += defeated_in_current_city
        B[i] -= defeated_in_current_city

        # 勇者 i が残りの力で街 i+1 のモンスターを倒す
        defeated_in_next_city = min(A[i + 1], B[i])
        ans += defeated_in_next_city
        A[i + 1] -= defeated_in_next_city

    return ans


# 入力の読み取り
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 結果の出力
print(max_monsters_defeated(N, A, B))

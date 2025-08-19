# AI生成
def main():
    n = int(input())
    s = input()
    mx = [0] * 26  # アルファベット26文字用の配列
    l = 0

    while l < n:
        r = l + 1
        while r < n and s[l] == s[r]:
            r += 1
        c = ord(s[l]) - ord('a')  # 文字をインデックスに変換
        mx[c] = max(mx[c], r - l)  # 最大値を更新
        l = r

    ans = sum(mx)  # 結果を合計
    print(ans)

if __name__ == "__main__":
    main()

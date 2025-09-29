# AI生成
from itertools import combinations

def main():
    K = int(input())
    nums = []
    # 1桁～10桁まで（0～9の10個の数字）
    for d in range(1, 11):
        for comb in combinations(range(10), d):
            # 上から順に並べるには逆順にして数字を作る
            print(comb)
            num = 0
            for c in comb[::-1]:
                num = num * 10 + c
            if num > 0:  # 0始まりは除外
                nums.append(num)
    nums.sort()
    print(nums[K-1])

if __name__ == "__main__":
    main()

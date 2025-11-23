# 解説写してコメントを加えた
N,K,X=map(int,input().split())
S=[input() for _ in range(N)]

ans=[]

def dfs(crr, count):
  # count 個の文字列を結合して crr になった状態
  if count==K:
    ans.append(crr)
    return
  for s in S:
    dfs(crr+s, count+1)

dfs("", 0)
# 辞書順に並び替える
ans.sort()
print(ans[X-1])

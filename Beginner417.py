from collections import Counter

n = int(input())
A = list(map(int,input().split()))
Ai_plus_i = Counter(i+A[i] for i in range(n))
print(sum(Ai_plus_i[j-A[j]] for j in range(n)))

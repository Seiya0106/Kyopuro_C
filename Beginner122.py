n, q = map(int, input().split())
S = input()

p = [0] * (n+1)
for i in range(n-1):
    if S[i] == "A" and S[i+1] == "C":
        p[i+1] += p[i] + 1
    else:
        p[i+1] += p[i]
p[n] = p[n-1]

for _ in range(q):
    l, r = map(int, input().split())
    print(p[r-1] - p[l-1])  

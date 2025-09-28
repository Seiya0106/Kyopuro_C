from itertools import permutations

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
ord_list = list(range(1, N + 1))
cnt = 0
a = 0
b = 0
for i in permutations(ord_list):
    cnt += 1
    if i == tuple(P):
        a = cnt
    if i == tuple(Q):
        b = cnt
print(abs(a-b))

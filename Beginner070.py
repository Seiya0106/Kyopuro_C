import math

N = int(input())
T = []
for _ in range(N):
    T.append(int(input()))
print(math.lcm(*T))

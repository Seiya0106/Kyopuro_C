N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ans_a = 0
ans_b = 0
food_a = 0
food_b = 0

for _ in range(N):
  topa = max(A)
  food_a += topa
  A.remove(topa)
  ans_a += 1
  if food_a > X:
    break
  
for _ in range(N):
  topb = max(B)
  food_b += topb
  B.remove(topb)
  ans_b += 1
  if food_b > Y:
    break

print(min(ans_a, ans_b))

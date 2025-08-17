N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
ans_a = 0
ans_b = 0
food_a = 0
food_b = 0

for a in A:
    food_a += a
    ans_a += 1
    if food_a > X:
        break
for b in B:
    food_b += b
    ans_b += 1
    if food_b > Y:
        break

print(min(ans_a, ans_b))

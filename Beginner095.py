A, B, C, X, Y = map(int, input().split())
normal = A * X + B * Y
abmin = min(X, Y)
abmax = max(X, Y)
# A, Bの最小の数だけABを買う場合
moneymin = C * abmin * 2
X -= abmin
Y -= abmin
if X < Y:
    moneymin += B * Y
else:
    moneymin += A * X
# A, Bの最大の数だけABを買う場合
moneymax = C * abmax * 2

if normal < moneymin and normal < moneymax:
    print(normal)
elif moneymin < normal and moneymin < moneymax:
    print(moneymin)
else:
    print(moneymax)

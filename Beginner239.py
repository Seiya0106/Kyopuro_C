# 手動だから効率が悪い
x1, y1, x2, y2 = map(int, input().split())
x = abs(x1 - x2)
y = abs(y1 - y2)

if (x == 1 and y == 3) or (x == 3 and y == 1) or\
    (x == 1 and y == 1) or (x == 3 and y == 3) or\
        (x == 0 and y == 2) or (x == 2 and y == 0) or\
            (x == 0 and y == 4) or (x == 4 and y == 0) or\
                (x == 2 and y == 4) or (x == 4 and y == 2):
    print("Yes")
else:
    print("No")

n, q = map(int,input().split())
ball = [i for i in range(1, n+1)]
pos = {i:i-1 for i in range(1, n+1)}
for _ in range(q):
    x = int(input())
    current_pos = pos[x]

    if current_pos == n - 1:
        left_pos = current_pos - 1
        ball[current_pos], ball[left_pos] = ball[left_pos], ball[current_pos]
        pos[ball[current_pos]] = current_pos
        pos[ball[left_pos]] = left_pos
    else:
        right_pos = current_pos + 1
        ball[current_pos], ball[right_pos] = ball[right_pos], ball[current_pos]
        pos[ball[current_pos]] = current_pos
        pos[ball[right_pos]] = right_pos

print(*ball)

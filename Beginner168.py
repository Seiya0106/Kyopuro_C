import math

a, b, h, m = map(int, input().split())
hour = h * 30 + m * 0.5
minute = m * 6
angle = abs(hour - minute)
if angle > 180:
    angle = 360 - angle
cos = math.cos(math.radians(angle))
length = a ** 2 + b ** 2 - 2 * a * b * cos
print(math.sqrt(length))

# TLE
import sys
input = sys.stdin.readline
K = int(input())
cnt = 0
num = 0

while cnt < K:
    num += 1
    number = str(num)
    length = len(number)
    if length == 1:
        cnt += 1
    else:
        for i in range(length - 1):
            if number[i]  <= number[i + 1]:
                break
            elif i == length - 2:
                cnt += 1
print(num)

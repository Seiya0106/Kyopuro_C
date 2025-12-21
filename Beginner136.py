n = int(input())
H = list(map(int, input().split()))
under = H[0]
for i in range(1, n):
    if H[i] < under:
        print("No")
        exit()
    elif H[i] == under:
        continue
    else:
        under = H[i] - 1
print("Yes")

from itertools import groupby

s = input()
t = input()
if len(s) > len(t):
    print("No")
    exit()
a = [(v, len(list(x))) for v, x in groupby(s)]
b = [(v, len(list(x))) for v, x in groupby(t)]

# グループ数が不一致の時には成り立たない
# この部分は思いつかなかったため、AIに聞いて納得した部分
if len(a) != len(b):
    print("No")
    exit()
  
for i in range(len(a)):
    if a[i][0] == b[i][0]:
        if a[i][1] == b[i][1]:
            continue
        elif a[i][1] == 1 and a[i][1] != b[i][1]:
            print("No")
            exit()
        elif a[i][1] > b[i][1]:
            print("No")
            exit()
    else:
        print("No")
        exit()
print("Yes")

S = input()

while len(S) > 0:
    if S.endswith("dreamer"):
        S = S[:-len("dreamer")]
    elif  S.endswith("dream"):
        S = S[:-len("dream")]
    elif S.endswith("eraser"):
        S = S[:-len("eraser")]
    elif S.endswith("erase"):
        S = S[:-len("erase")]
    else:
        print("NO")
        exit()

print("YES")

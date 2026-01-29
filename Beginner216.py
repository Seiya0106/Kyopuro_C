n = int(input())
result = []

while n > 0:
    if n % 2 != 0:
        result.append("A")
        n -= 1
    else:
        result.append("B")
        n = n // 2

result.reverse()
print("".join(result))

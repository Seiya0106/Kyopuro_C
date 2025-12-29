x = input()
n = int(input())
names = []
for _ in range(n):
    names.append(input())

order = {}
for k, v in enumerate(x):
    order[v] = k

def custom_sort_key(s):
    return [order[c] for c in s]

names.sort(key=custom_sort_key)

for name in names:
    print(name)

# AI生成
import sys

s = sys.stdin.readline().strip()
if not s:
    sys.exit()
digits = [int(c) for c in s]
k = len(digits)
r = sum(digits) % 3

if r == 0:
    print(0)
    sys.exit()

# If we can remove 1 digit with digit%3 == r (and still have at least 1 digit left)
if k >= 2 and any(d % 3 == r for d in digits):
    print(1)
    sys.exit()

# Otherwise try removing 2 digits with digit%3 == (3-r) (need at least 3 digits total)
if k >= 3 and sum(1 for d in digits if d % 3 == (3 - r)) >= 2:
    print(2)
    sys.exit()

print(-1)

import sys

line1 = sys.stdin.readline().strip()
arr = list(map(int, line1.split()))
n, s = arr[0], arr[1]

line2 = sys.stdin.readline().strip()
nums = list(map(int, line2.split()))

nums.sort()
cnt = 0

for n in nums:
    s -= n
    if s >= 0:
        cnt += 1
    else:
        break

print(cnt)


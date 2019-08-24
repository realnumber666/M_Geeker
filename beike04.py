import sys

n = int(sys.stdin.readline().strip())

line1 = sys.stdin.readline().strip()
nums = list(map(int, line1.split()))

ret = float("inf")
for i in range(n):
    tmp = 0
    top = 0
    for j in range(n):
        top = max(top, abs(j-i)+nums[j])

    for m in range(0, i):
        to = top-(i-m)
        if nums[m] < to:
            tmp+= to-nums[m]

    ret = min(ret, to_tol-sum(nums))

print(ret)
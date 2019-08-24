import sys

line1 = sys.stdin.readline().strip()
nums = list(map(int, line1.split()))

n = nums[0]
q = nums[1]

line1 = sys.stdin.readline().strip()
nums = list(map(int, line1.split()))

ret = []
for i in range(q):
    j = int(sys.stdin.readline().strip())
    cnt = 0
    for k in range(n):
        if nums[k] >= j:
            cnt += 1
            nums[k] -= 1
    ret.append(cnt)

for o in ret:
    print(o)
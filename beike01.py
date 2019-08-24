import sys

n = int(sys.stdin.readline().strip())

line1 = sys.stdin.readline().strip()
nums = list(map(int, line1.split()))

ret = []
tmp = None

for i in range(n-1):
    delt = abs(nums[i] - nums[i+1])
    if tmp is None:
        tmp = delt
        ret = [str(nums[i]), str(nums[i+1])]
    else:
        if tmp > delt:
            tmp = delt
            ret = [str(nums[i]), str(nums[i+1])]

print(' '.join(ret))
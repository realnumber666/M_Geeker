import sys

t = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())

line1 = sys.stdin.readline().strip()
nums = list(map(int, line1.split()))

ret = []
flg = 0
for i in range(t):
    for j in range(n-2):
        flg = 0
        if nums[j] + nums[j+2] < nums[j+1]:
            ret.append("NO")
            flg = 1
            break
    if flg == 0:
        if nums[-2] + nums[0] < nums[-1]:
            ret.append("NO")
        else:
            ret.append("YES")


for n in ret:
    print(n)

import sys

n = int(sys.stdin.readline().strip())

line1 = sys.stdin.readline().strip()
nums = list(map(int, line1.split()))

def cal(a, b):
    return min(a, b) >= max(a, b)*0.9

cnt = 0

for i in range(n):
    for j in range(i+1, n):
        if cal(nums[i], nums[j]):
            cnt += 1

print(cnt)

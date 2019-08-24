# -*- coding: UTF-8 -*-

import sys


def maxSum(nums):
    maxsum = 0
    maxtmp = 0
    for i in range(len(nums)):
        if maxtmp >= 0:
            maxtmp = nums[i]
        else:
            maxtmp += nums[i]

        maxsum = min(maxsum, maxtmp)

    return maxsum

# 读取第一行的n
n = sys.stdin.readline().strip()

# 读取每一行
line = sys.stdin.readline().strip()
# 把每一行的数字分隔后转化成int列表
values = list(map(int, line.split()))

if n == 0:
    print(0)

if n == 1:
    print(values[0])

ret = 0
for n in values:
    ret += n

need_to_del = maxSum(values)

print(ret - need_to_del)




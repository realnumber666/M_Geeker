# -*- coding: UTF-8 -*-

import sys

# 读取第一行的n
n = sys.stdin.readline().strip()

# 读取每一行
line = sys.stdin.readline().strip()
# 把每一行的数字分隔后转化成int列表
values = list(map(int, line.split()))

values.sort()
ret = values[0] + values[1]
ret /= 2
# print(ret)
# print(values)

for i in range(2, len(values)):
    # print("ret: ", ret)
    ret += values[i]
    ret /= 2

print(ret)
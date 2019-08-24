# -*- coding: UTF-8 -*-

import sys

a = sys.stdin.readline().split()
n, m = int(a[0]), int(a[1])

tol_arr = []
for i in range(n):
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    values = list(map(int, line.split()))
    tol_arr.append(values)

print(tol_arr[n-2][m-1] * tol_arr[n-1][m-2])
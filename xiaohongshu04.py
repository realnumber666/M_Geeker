import sys

line1 = sys.stdin.readline().strip().split()
arr1 = list(map(int, line1))
n, t, m = arr1[0], arr1[1], arr1[2]

line2 = sys.stdin.readline().strip().split()
arr2 = list(map(int, line2))

summ = sum(arr2)
if t < n:
    ret = -1
else:
    if t > m:
        summ -= t-m
        ret = int(summ//m) + 1
    else:
        ret = int(summ//t) + 1

print(ret)

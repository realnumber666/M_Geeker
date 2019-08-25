import sys

line1 = sys.stdin.readline().strip()
arr1 = list(map(int, line1.split()))
n, k = arr1[0], arr1[1]

arrs = []
line = sys.stdin.readline().strip()
arr = list(map(int, line.split()))

while line != '':
    arr = list(map(int, line.split()))
    arrs.append(arr)
    line = sys.stdin.readline().strip()

flg0 = 1
for arr in arrs:
    if arr[2] == 1:
        flg0 = 0

if flg0 == 1:
    print('0')
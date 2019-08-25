import sys

line1 = sys.stdin.readline().strip()
arr = list(map(int, line1.split()))
n, m = arr[0], arr[1]

line2 = sys.stdin.readline().strip()
nums = list(map(str, line2.split()))

dct = {}

for k in nums:
    if k not in dct:
        dct[k] = 1
    else:
        dct[k] += 1

keys = list(dct.keys())

for key in keys:
    if dct[key] > m:
        del dct[key]

ret = []
s_nums = []
for c in nums:
    if c not in s_nums:
        s_nums.append(c)

for k in s_nums:
    if k in dct:
        ret += k * dct[k]

ret_str = ' '.join(ret)
print(ret_str)
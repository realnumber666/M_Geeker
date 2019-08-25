import sys

n = int(sys.stdin.readline().strip())
arrs = []
ret = []
for _ in range(n):
    line1 = sys.stdin.readline().strip()
    arr = list(map(str, line1.split()))
    arrs.append(arr)

for arr in arrs:
    l = arr[0].split('.')
    r = arr[1].split('.')
    length = max(len(r), len(l))
    if len(l) <= len(r):
        l += ['0']*(len(r)-len(l))
    else:
        r += ['0']*(len(l) - len(r))
    i = 0
    flg = 0
    while i < length:
        if int(l[i]) < int(r[i]):
            ret.append('true')
            flg = 1
            break
        if int(l[i]) > int(r[i]):
            ret.append('false')
            flg = 1
            break
        i += 1
    if flg == 0:
        ret.append('false')

for r in ret:
    print(r)
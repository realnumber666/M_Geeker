import sys

line1 = sys.stdin.readline().strip()
arr = list(map(int, line1.split()))
n, m = arr[0], arr[1]
shell = []

for _ in range(n):
    line = sys.stdin.readline().strip()
    arrs = list(map(int, line.split()))
    shell.append(arrs)

cnt = 0
for sh in shell:
    scount = sh[0]
    ssize = sh[1]
    tmp = m // ssize
    if tmp == 0:
        break
    if tmp <= scount:
        cnt += tmp
        m -= tmp*ssize
    else:
        cnt += scount
        m -= scount*ssize

print(cnt)
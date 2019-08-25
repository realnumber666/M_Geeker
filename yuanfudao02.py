import sys

n = int(sys.stdin.readline().strip())
tol_arrs = []
for _ in range(n):
    line = sys.stdin.readline().strip()
    arrs = list(map(int, line.split()))
    tol_arrs.append(arrs[1:])

cnt = []
for arr in tol_arrs:
    arr.sort()
    length = len(arr)
    tmp_cnt = 0
    for i in range(length):
        if arr[i] > 0:
            break

    while length-i >= 3:
        tmp_cnt += arr[i]
        to_del = arr[i]
        for k in range(i, length):
            arr[k] -= to_del

        for i in range(length):
            if arr[i] > 0:
                break
    cnt.append(tmp_cnt)

for n in cnt:
    print(str(n))

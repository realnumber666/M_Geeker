import sys

n = int(sys.stdin.readline().strip())

line1 = sys.stdin.readline().strip()
scores = list(map(int, line1.split()))

q = int(sys.stdin.readline().strip())
tol_ret = []
for i in range(q):
    idx = int(sys.stdin.readline().strip())
    score = scores[idx-1]
    cnt = 0
    for m in scores:
        if m < score:
            cnt += 1
    if cnt == 0:
        tol_ret.append(format(0, "0.6f"))
    else:
        ret = round((cnt / n)*100, 6)
        tol_ret.append(ret)


for n in tol_ret:
    print(n)
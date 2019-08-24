import sys

line = sys.stdin.readline().strip().split()
n = int(line[0])
arr = line[1]
arr = list(map(int, arr[1:-1].split(",")))
ret = 0
sett = []
def shuquan(n, arr, ans):
    global ret
    global sett
    for k in arr:
        ans.append(k)
        t = n - k
        if t < 0:
            ans = []
            continue
        elif t == 0:
            ret += 1
        else:
            shuquan(t, arr,ans)
shuquan(n, arr, [])
print(ret)
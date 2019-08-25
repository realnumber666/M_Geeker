import sys

line1 = sys.stdin.readline().strip()
arr1 = list(map(str, line1.split()))

line2 = sys.stdin.readline().strip()
arr2 = list(map(str, line2.split()))

cnt = int(len(arr1)//4)
ret = ['']*(cnt*5)
if len(arr2) == 0:
    print(' '.join(arr1))
else:
    for i in range(cnt):
        for j in range(4):
            ret[j+i*5] = arr1[j+i*4]
        if i+1 <= len(arr2):
            ret[4+i*5] = arr2[i]

    if len(arr1)> 4*cnt:
        ret += arr1[-(len(arr1)-4*cnt):]

    if len(arr2)>cnt:
        ret += arr2[-(len(arr2)-cnt):]
    if '' in ret:
        ret.remove('')
    print(' '.join(ret))
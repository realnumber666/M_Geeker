import sys

line1 = sys.stdin.readline().strip()
arr = list(map(int, line1.split()))
n, s = arr[0], arr[1]

line2 = sys.stdin.readline().strip()
cnt = -1
tmp = ''
flg = 1
if n == 0 or line2 == '':
    print('')
else:
    for c in line2:
        if tmp == '':
            tmp = c
        else:
            if tmp != c:
                flg = 0
                break
            tmp = c
    if flg == 1:
        print(line2[0]*(s-1)+line2)
    else:
        for i in range(n):
            l = line2[:n-1-i]
            r = line2[i+1:]
            if l == r and l != '':
                if cnt == -1:
                    cnt = n-i-1
                else:
                    cnt = min(n-i-1, cnt)

        if cnt == -1:
            print(line2*s)
        else:
            print(line2[:cnt+1]*(s-1)+line2)
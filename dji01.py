import sys

ret = []

while True:
    line1 = sys.stdin.readline().strip('\n')
    if line1 == '':
        break
    nums = list(map(int, line1.split()))
    N, A, X = nums[0], nums[1], nums[2]

    line2 = sys.stdin.readline().strip('\n')
    bugs = list(map(int, line2.split()))

    raw_time = sum(bugs)
    up = A*X*60
    if raw_time > up:
        ret.append(raw_time-up+(up//A))
    else:
        if raw_time % A != 0:
            time = raw_time//A + 1
            if time > 480:
                ret.append(0)
            else:
                ret.append(time)
        else:
            time = raw_time//A
            if time > 480:
                ret.append(0)
            else:
                ret.append(time)


for n in ret:
    print(n)


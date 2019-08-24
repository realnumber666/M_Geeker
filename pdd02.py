import sys

line1 = sys.stdin.readline().strip()
A = list(map(str, line1.split()))
if len(A) == 0:
    print("false")
else:
    c_dct = {}

    for s in A:
        l = s[0]
        r = s[-1]

        if l not in c_dct:
            c_dct[l] = 1
        else:
            c_dct[l] += 1
        if r not in c_dct:
            c_dct[r] = 1
        else:
            c_dct[r] += 1

    flg = 0
    for n in c_dct.values():
        if n % 2 != 0:
            print("false")
            flg = 1
            break

    if flg == 0:
        print("true")
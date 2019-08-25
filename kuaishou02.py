import sys

n = int(sys.stdin.readline().strip())
nums = []
ret = []
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    nums.append(num)

def isToOne(num):
    dct = {}
    summ = num
    while summ not in dct:
        dct[summ] = True
        summ = 0
        while num:
           summ += pow(num%10, 2)
           num //= 10
        num = summ

    if summ == 1:
        return 'true'
    else:
        return 'false'

for num in nums:
    print(isToOne(num))

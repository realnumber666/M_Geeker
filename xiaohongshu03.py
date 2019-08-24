import sys

n = int(sys.stdin.readline().strip())

line = sys.stdin.readline().strip().split()
arr = list(map(int, line))

sum1 = 0
sum2 = 0
cnt = int(len(arr)//2)
i = 0
j = 1
while i < len(arr):
    sum1 += arr[i]
    i += 2

while j < len(arr):
    sum2 += arr[j]
    j += 2

if sum1 > sum2:
    if len(arr) % 2 != 0:
        cnt = int(len(arr)//2+1)

print(max(sum1, sum2), cnt)
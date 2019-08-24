import sys

line = sys.stdin.readline().strip()
nums = list(map(int, line.split()))
n = nums[0]
k = nums[1]

line = sys.stdin.readline().strip()
arr = list(map(int, line.split()))

left = 0
right = 0
length = 0
summ = arr[0]

while right < len(arr):
    if summ == k:
        length = max(right - left + 1, length)
        summ -= arr[left]
        left += 1
    elif summ < k:
        right += 1
        if right == len(arr):
            break
        summ += arr[right]
    else:
        left += 1
        summ -= arr[left]

print(length)

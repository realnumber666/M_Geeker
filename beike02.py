import sys

n = int(sys.stdin.readline().strip())
nums = []

for _ in range(n):
    k = int(sys.stdin.readline().strip())
    nums.append(k)

subarr = []
subarr.append(nums[0])
def binarySearch(arr, num, l, r):
    if l == r:
        return l
    while l < r:
        mid = (l+r) // 2
        if mid == l or mid == r:
            if num > arr[l]:
                return r
            else:
                return l
        if num < arr[mid]:
            return binarySearch(arr, num, l, mid)
        else:
            return binarySearch(arr, num, mid, r)

for i in range(1, len(nums)):
    if nums[i] > subarr[-1]:
        subarr.append(nums[i])
    elif nums[i] < subarr[0]:
        subarr[0] = nums[i]
    else:
        pos = binarySearch(subarr, nums[i], 0, len(subarr)-1)
        subarr[pos] = nums[i]

print(len(subarr))



import itertools
import sys

n = int(sys.stdin.readline().strip())

line1 = sys.stdin.readline().strip()
nums = list(map(int, line1.split()))

m = n // 2
ret = float('inf')
ret_arr = None
for i in range(1, n+1):
    combs = list(list(itertools.combinations(nums,i)))
    for comb in combs:
        comb = list(comb)
        if abs(sum(nums) - 2*sum(comb)) < ret:
            ret = abs(sum(nums) - 2*sum(comb))
            ret_arr = comb

print(ret, abs(n-2*len(ret_arr)))
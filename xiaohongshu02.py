import sys

line = sys.stdin.readline().strip().split()
arr = list(map(str, line))
arr = arr[::-1]
print(" ".join(arr))
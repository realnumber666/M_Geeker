import sys
line1 = sys.stdin.readline().strip()
A = list(map(int, line1.split()))

line2 = sys.stdin.readline().strip()
B = list(map(int, line2.split()))

# print(A, B)
for i in range(len(A)):
    if A[i] > A[i + 1]:
        break

left = A[i]
right = A[i + 2] if i+1 < len(A) - 1 else float('inf')
B.sort()
# print(left, right)
flg = 0
for j in range(len(B)):
    n = B[len(B) - 1 - j]
    if n < right and n > left:
        A[i+1] = n
        flg = 1
        break

if flg == 0:
    print("NO")
else:
    print(' '.join(str(i) for i in A))

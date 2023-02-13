'''
import sys

N = int(input())
arr = list(map(int,sys.stdin.readline().split()))
nge = False
answer = []

for i in range(len(arr)) :
    for j in range(i+1,len(arr)) :
        if arr[j] > arr[i] :
            answer.append(str(arr[j]))
            nge = True
            break
    if not nge :
        answer.append(str(-1))
    nge = False

print(' '.join(answer))
'''

import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)
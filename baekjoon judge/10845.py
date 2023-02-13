import sys
from collections import deque

N = int(input())
commend = [[] for i in range(N)]
for i in range(N) :
    commend[i] = list(sys.stdin.readline().split())
queue = deque([])

for i in range(len(commend)) :
    if commend[i][0] == 'push' :
        queue.append(commend[i][1])
    if commend[i][0] == 'pop':
        if not queue :
            print(-1)
        else :
            print(queue.popleft())
    if commend[i][0] == 'size' :
        print(len(queue))
    if commend[i][0] == 'empty' :
        if not queue :
            print(1)
        else :
            print(0)
    if commend[i][0] == 'front' :
        if not queue :
            print(-1)
        else :
            print(queue[0])
    if commend[i][0] == 'back' :
        if not queue :
            print(-1)
        else :
            print(queue[-1])
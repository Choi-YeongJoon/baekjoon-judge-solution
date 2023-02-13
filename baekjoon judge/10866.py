import sys
from collections import deque

queue = deque()
N = int(input())
commend = [[] for i in range(N)]
for i in range(N) :
    commend[i] = list(sys.stdin.readline().split())

for i in range(N) :
    if commend[i][0] == 'push_back' :
        queue.append(commend[i][1])
    elif commend[i][0] == 'push_front' :
        queue.insert(0,commend[i][1])
    elif commend[i][0] == 'pop_front' :
        if queue:
            print(queue.popleft())
        else : print(-1)
    elif commend[i][0] == 'pop_back' :
        if queue:
            print(queue.pop())
        else : print(-1)
    elif commend[i][0] == 'size' :
        print(len(queue))
    elif commend[i][0] == 'empty' :
        if queue :
            print(0)
        else :
            print(1)
    elif commend[i][0] == 'front' :
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif commend[i][0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)



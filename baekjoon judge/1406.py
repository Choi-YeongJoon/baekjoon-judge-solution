#문제출처 : https://www.acmicpc.net/problem/1406
#재풀이 필요

import sys

string_A = sys.stdin.readline().rstrip()
curser = len(string_A) - 1
N = int(input())
commend = [[] for i in range(N)]
for i in range(N) :
    commend[i] = list(sys.stdin.readline().split())

for i in range(len(commend)) :
    for editor in commend[i][0] :
        if editor == 'L' and curser > 0 :
            curser -= 1
            print(string_A)
        elif editor == 'R' and curser < len(string_A) :
            curser += 1
            print(string_A)
        elif editor == 'B' and curser >= 0 :
            string_A = string_A[0:curser] + string_A[curser+1:]
            if curser <= 1:
                curser -= 1
            print(string_A)
        elif editor == 'P' :
            string_A = string_A[0:curser] + commend[i][1] + string_A[curser+1:]
            curser += 1
            print(string_A)

print(string_A)
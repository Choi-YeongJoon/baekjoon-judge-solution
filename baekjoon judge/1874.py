#문제출처 : https://www.acmicpc.net/problem/1874

import sys

N = int(input())
#point:시작점 / stack:중간에 사용하는 스택 / arr:주어진 수열
point, stack, arr = 1, [], []
#answer:정답(+,-)배열, posible:수열 생성 가능여부
answer, posible = [], True
for i in range(N) :
    arr.append(int(sys.stdin.readline().rstrip()))

#주어진 수열 순서대로 실행
for i in arr :
    #포인트가 수열보다 작으면 포인트 올려주면서 정답 stack
    while i >= point :
        stack.append(point)
        point += 1
        answer.append('+')
    #마지막 스택을 팝하면서 정답 stack
    if stack[-1] == i :
        stack.pop()
        answer.append('-')
    #오름차순으로 스택했으므로 마지막 자리가 주어진 수열과 다르면 수열 생성 불가
    else :
        posible = False

if posible :
    print('\n'.join(answer))
else :
    print('NO')
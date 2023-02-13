#문제출처 : https://www.acmicpc.net/problem/9012
#시간제한 : 1초 / 메모리제한 : 128MB
#시간복잡도 : O(N)=50*T < 200,000 / 공간복잡도 : 최대 4byte*50*T (문제에서 주어지지 않음)

import sys

#입력 및 초기화
N = int(input())
vps = [0] * N
#str 끝 개행(\n) 지운 후 리스트로 저장 : str.rstrip()
for i in range(N) :
    vps[i] = sys.stdin.readline().rstrip()
is_vps = [False] * len(vps)
tf_vps = 0

for i in range(N) :
    for j in vps[i] :
        #괄호 )가 먼저 나올 시 VPS 아님
        if tf_vps < 0 :
            tf_vps = -50
        #괄호 짝 맞추어 나올 시 VPS
        if j == "(" :
            tf_vps += 1
        elif j == ")" :
            tf_vps -= 1
    if tf_vps == 0 :
        is_vps[i] = 'YES'
    else :
        is_vps[i] = 'NO'
    #줄마다 VPS 판단 초기화
    tf_vps = 0

print('\n'.join(is_vps))
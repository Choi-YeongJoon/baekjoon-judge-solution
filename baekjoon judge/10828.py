# 문제출처 : https://www.acmicpc.net/problem/10828
# 시간제한 : 0.5초 / 메모리제한 : 256MB
# 시간복잡도 : O(N), 공간복잡도 최대 20byte(push명령)*10000 = 200KB (∵ 1 ≤ N ≤ 10,000, 정수는 100,000이하)

N = int(input())
commend = [0]*N #명령어 리스트
list_A = [] #데이터 리스트

for i in range(N) :
    commend[i] = list(input().split()) #커맨드 명령어 리스트로 저장

for i in range(N) : #명령어에 대한 수행
    if commend[i][0] == 'push' : list_A.append(int(commend[i][1])) #데이터 삽입
    if commend[i][0] == 'pop' :
        if not list_A : #데이터 리스트 비었을 경우
            print(-1)
        else : #데이터 리스트에 데이터 존재할 경우
            print(list_A.pop())
    if commend[i][0] == 'size' : print(len(list_A))
    if commend[i][0] == 'empty' :
        if not list_A :
            print(1)
        else :
            print(0)
    if commend[i][0] == 'top' :
        if not list_A :
            print(-1)
        else :
            print(list_A[len(list_A)-1]) #가장 윗단의 데이터 출력 (인덱스 : 리스트 길이 - 1)
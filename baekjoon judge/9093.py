#문제출처 : https://www.acmicpc.net/problem/9093
#시간제한 : 1초 / 메모리제한 : 128MB
#시간복잡도 : O(2N) < 0.5초, 공간복잡도 : 4byte*20000 = 80KB
import sys

#초기화 및 입력
N = int(input())
word_list = [[] for _ in range(N)]
rev_word_list = [[] for _ in range(N)]
for i in range(N) :
    word_list[i] = list(sys.stdin.readline().split())

# 리스트 내 문자에 한 개씩 접근하여 문자열 슬라이싱
for i in range(N) :
    for j in range(len(word_list[i])) :
        print(word_list[i][j][::-1], end = ' ')
    print(end='\n')

#문자열 뒤집는 방법
#1. 문자열 슬라이싱 str_list[::-1]
#2. 반복문 for i in str_list (rev_str_list = i + rev_str_list)
#3. 리버스 함수 list.reverse() → 리스트 뒤집는 함수, 출력 시 print(''.join(list))
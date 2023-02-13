import sys

sentence = sys.stdin.readline()
#역순출력 : stack, 정상출력 : answer
stack, answer = [], []
rev = True

for i in sentence :
    # 조건 2, 3
    if i == '<' or i == ' ' :
        while stack :
            answer.append(stack.pop())
        answer.append(i)
        if i == '<' : rev = False
    # 조건 2
    elif i == '>' :
        rev = True
        answer.append(i)
    # 줄바꿈 문자는 스킵
    elif i == '\n' :
        continue
    else :
        if not rev :
            answer.append(i)
        else :
            stack.append(i)

# 스택에 남아 있는 문자 역순 출력
while stack :
    answer.append(stack.pop())

print(''.join(answer))

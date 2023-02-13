import sys

N = int(input())
eaq = list(sys.stdin.readline())
del eaq[-1]
dict = {}
for i in range(N) :
    dict[chr(ord('A')+i)] = int(input())

stack = []

for i in eaq :
    if i >= 'A' and i <= 'Z' :
        stack.append(dict[i])
    else :
        if i == '+' :
            stack.append(stack.pop(-2) + stack.pop(-1))
        elif i == '-':
            stack.append(stack.pop(-2) - stack.pop(-1))
        elif i == '*':
            stack.append(stack.pop(-2) * stack.pop(-1))
        else :
            stack.append(stack.pop(-2) / stack.pop(-1))

print("{:.2f}".format(stack[0]))
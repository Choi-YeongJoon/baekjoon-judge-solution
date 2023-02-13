N, K = map(int,input().split())
begin = 0
numbers = [i+1 for i in range(N)]
yosepus = []
answer = []

while numbers :
    begin = begin + (K - 1)
    if begin >= len(numbers) :
        begin = begin % len(numbers)
    yosepus.append(numbers.pop(begin))

for i in yosepus :
    answer.append(str(i))

print('<' + ', '.join(answer) + '>')
import sys

S = list(sys.stdin.readline())
del S[-1]

answer = [0] * (ord('z') - ord('a') + 1)

for i in S :
    answer[ord(i) - ord('a')] += 1

print(*answer)
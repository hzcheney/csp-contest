import sys

n = int(input())
sum = 0

while True:
    w_i, score_i = map(int, sys.stdin.readline().split())
    sum += score_i * w_i
    n -= 1
    if n == 0:
        break

if sum < 0:
    print(0)
else:
    print(sum)


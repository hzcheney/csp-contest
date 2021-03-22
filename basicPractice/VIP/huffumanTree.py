import sys

def step(L = None):
    min1 = min(L)
    L.remove(min1)
    min2 = min(L)
    L.remove(min2)

    sum = min1 + min2
    L.insert(1, sum)
    return sum

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
sum = 0
while True:
    if len(nums) != 1:
        sum = sum + step(nums)
    else:
        break

print(sum)


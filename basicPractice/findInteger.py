import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
num = int(sys.stdin.readline())

try:
    ret = nums.index(num) + 1
except ValueError:
    ret = -1
print(ret)

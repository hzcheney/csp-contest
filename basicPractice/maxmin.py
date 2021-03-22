import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

print(max(nums))
print(min(nums))
print(sum(i for i in nums))

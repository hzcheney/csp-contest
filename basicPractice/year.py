import sys
year = int(sys.stdin.readline())
if (year % 4) == 0 and (year % 100 !=0):
    print('yes')
elif year % 400 ==0:
    print('yes')
else:
    print('no')

import sys

rows, columns = map(int, sys.stdin.readline().split())
# line = [chr(ord('A') + i) for i in range(columns)]
line = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
if  1 <= rows <= 26 and 1 <= columns <= 26:
    for i  in range(rows):
        rear = line[1: i + 1]
        front = line[0: columns - i]
        s = rear[::-1] + front
        print(s[0:columns])


length = int(input())
n = 0
while n < length:
    hexNum = input()
    if hexNum != '':
        print(format(int(hexNum, 16), 'o'))
        n += 1
    else:
        break


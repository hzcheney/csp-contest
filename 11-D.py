row = 0
column = 0
num = 0
while True:
    num += 1
    if row == 19 and column == 19:
        break
    if (row + column) & 1:
        ## 奇数的情况
        row += 1
        if column > 0:
            column -= 1
    else:
        column += 1
        if row > 0:
            row -= 1
print(num)

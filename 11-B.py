def check(s):
    return s == '2020'


matrix = []
s = input()
while '1' not in s:
    matrix.append(list(s))
    s = input()
n, m = len(matrix), len(matrix[0])
ans, row, column = 0, 0, 0
for i in range(n):
    for j in range(m):
        # 判断每一列的 2020 数量
        # print(str(matrix[i][j:j + 4]))
        if i + 3 < n and check(matrix[i][j] + matrix[i + 1][j] + matrix[i + 2][j] + matrix[i + 3][j]):
            # if i + 3 < n and check(str(matrix[i:i + 4][j])):
            ans += 1
            column += 1
        # 判断每一行的 2020 数量
        # If we use martrix[i][j:j + 4] here,then we will
        # if j + 3 < m and check(matrix[i][j] + matrix[i][j + 1] + matrix[i][j + 2] + matrix[i][j + 3]):
        if j + 3 < m and check(str(matrix[i][j:j + 4])):
            ans += 1
            row += 1
        # 判断左上到右下的 2020 数量
        if i + 3 < n and j + 3 < m and check(
                matrix[i][j] + matrix[i + 1][j + 1] + matrix[i + 2][j + 2] + matrix[i + 3][j + 3]):
            ans += 1
print(ans)

from sys import stdin


def readint():
    return int(stdin.readline())


def readarray(typ):
    return list(map(typ, stdin.readline().split()))


def readmatrix(n):
    M = []
    for _ in range(n):
        row = readarray(int)
        assert len(row) == 2 # This determines the number of input per line
        M.append(row)
    return M


def judge(theta, l = None):
    ans = 0
    if l is None:
        l = []
    for row in l:
        y_i = row[0]
        result_i = row[1]
        if y_i < theta and result_i == 0:
            ans += 1
        elif y_i >= theta and result_i == 1:
            ans += 1
    return ans


if __name__ == '__main__':
    n = readint()
    A = readmatrix(n)
    best_theta = {}

    for row in A:
        theta = row[0]
        best_theta[theta] = judge(theta, A)

    _max = max([v for k, v in best_theta.items()])
    print(max([k for k, v in best_theta.items() if v == _max]))

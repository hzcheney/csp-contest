# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    mapL = [[0] * 4 for _ in range(7)]
    print(mapL)
    import time

    n = 206
    for i in range(n):
        m = int((i + 1) / n * 60)
        progressbar = '\r{} / {}, |{}>{}|'.format(i + 1, n, '=' * m, '-' * (60 - m))
        print(progressbar, end='')
        time.sleep(0.05)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

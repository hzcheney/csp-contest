import sys

total = int(input())
current_num = 0
current_sum = 0
def command(s, num):

    return

def transfer(num):

    return

while total != 0:
    command_str = list(map(str, sys.stdin.readline().split()))
    if command_str[0] == 'CLEAR':
        current_num = 0
    elif command_str[0] == 'EQUAL':
        print(current_sum)
    else:
        break


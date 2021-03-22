n = int(input())
for i in range(10000,1000000):
    num = str(i)
    if num == num[::-1]:
        if n == sum(int(i) for i in num):
            print(num)

for num in range(100, 1000):
    if num == sum(int(i)**3 for i in str(num)):
        print(num)

ans = 0
for i in range(1, 2021):
    ans += (str(i).count('2'))
print(ans)

print(''.join(str(j) for j in range(1, 2021)).count('2'))

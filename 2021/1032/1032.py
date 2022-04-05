N = int(input())
str1 = list(input())

for i in range(N-1):
    temp = list(input())
    for j in range(len(str1)):
        if str1[j] != temp[j]:
            str1[j] = '?'

print(''.join(str1))


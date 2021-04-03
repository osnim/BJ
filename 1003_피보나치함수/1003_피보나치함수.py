T = int(input()) #테스트 케이스 횟수

def fibonacci(num):
    if num == 0:
        print(list1[0][0], list1[0][1])

    elif num == 1:
        print(list1[1][0], list1[1][1])

    else:
        #재귀함수 쓰니 시간초과 발생
        #fibonacci(num - 1)
        #fibonacci(num - 2)

        for i in range(2, num+1):

            temp = list()
            temp = [i + j for i, j in zip(list1[i-2], list1[i-1])]
            list1.append(temp)

        print(list1[num][0], list1[num][1])

for _ in range(T):
    N = [0, 0]
    n = int(input())  # 테스트 케이스
    list1 = [[1, 0], [0, 1]] #[0호출 횟수, 1호출 횟수]

    fibonacci(n)


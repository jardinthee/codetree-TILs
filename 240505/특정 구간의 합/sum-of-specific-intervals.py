n , m = map(int,input().split())
A = list(map(int,input().split()))


def system(num):
    global A
    answer = []
    for i in range(num):
        a1 , a2 = map(int,input().split())
        answer.append(plus(a1,a2))
    for j in range(len(answer)):
        print(answer[j])


def plus(a1,a2):
    global A
    return sum(A[a1-1:a2])

system(m)
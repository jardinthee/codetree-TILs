N = int(input())

def cal(N):
    val = 0
    for i in range(1,N+1):
        val += i
    total = val//10
    return total

T=cal(N)

print(T)
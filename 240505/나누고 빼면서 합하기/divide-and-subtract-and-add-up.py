n , m = map(int,input().split(" "))
A = list(map(int,input().split(" ")))


def sys(num,list_):
    val = 0
    while num >= 1:
        val += A[num-1]
        
        if num % 2 == 1:
            num -= 1
            
        elif num % 2 == 0:
            num = num//2
            
    print(val)

sys(m,A)
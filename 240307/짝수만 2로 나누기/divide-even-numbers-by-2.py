N = int(input())
N_list = list(map(int,input().split()))

def pro(N,N_list):
    for n in range (N):
        if N_list[n] %2 ==0:
            N_list[n] //= 2
    N_list = list(map(int,N_list))

pro(N,N_list)

for i in N_list:
    print(i , end=" ")
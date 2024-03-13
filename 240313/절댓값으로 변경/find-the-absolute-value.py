N = int(input())
N_list = list(map(int,input().split()))

def absol(N,N_list):
    for i in range(N):
        if N_list[i] < 0:
            N_list[i] = -(N_list[i])
        else:
            pass
    for j in range(N):
        print(N_list[j],end=" ")

absol(N,N_list)
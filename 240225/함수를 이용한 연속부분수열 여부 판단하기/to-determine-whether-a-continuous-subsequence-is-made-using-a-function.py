n1, n2 = map(int,input().split(" "))
list_A= list(map(int,input().split(" ")))
list_B = list(map(int,input().split(" ")))


def seq(n1,n2,list_A,list_B):
    if n1 < n2:
        return False
    for i in range(int(n1)):
        if list_A[i:i+n2] == list_B:
            print('Yes')
            break
    else:
        print('No')


seq(n1,n2,list_A,list_B)
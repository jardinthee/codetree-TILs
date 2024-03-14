A = list(input())



def many(A):
    alist = []
    for i in range(len(A)):
        if A[i] in alist:
            pass
        else:
            alist.append(A[i])
    if 2 <= len(alist):
        print("Yes")
    else:
        print("No") 


many(A)
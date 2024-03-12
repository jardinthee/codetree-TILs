A = input()

def is_pal(N):
    list_a=[]
    for i in N[::-1]:
        list_a.append(i)
    a = "".join(list_a)
    if a == N:
        return True
    else:
        return False

if is_pal(A):
    print("Yes")
else:
    print("No")
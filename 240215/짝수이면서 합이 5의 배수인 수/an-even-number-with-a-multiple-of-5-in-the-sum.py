n = int(input())

def machine(n):
    a= str(n)

    if n%2 == 0 and (int(a[0])+int(a[1])) % 5 == 0:
        print('Yes')

    else:
        print('No')



machine(n)
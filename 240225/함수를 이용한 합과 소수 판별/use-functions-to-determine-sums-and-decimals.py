a,b = map(int,input().split(" "))


def is_sosu(n):
    nlist = []
    for i in range(1,100):
        if n%i ==0:
            nlist.append(i)
    if len(nlist) == 2:
        return True
    else:
        return False


def every_cal(n):
    n = str(n)
    val = 0
    for i in range(len(n)):
        val+= int(n[i])
    if val % 2 ==0:
        return True
    else:
        return False


def program(a,b):
    value = 0
    for i in range(a,b+1):
        if is_sosu(i) == True and every_cal(i) == True:
            value += 1
    print(value)


program(a,b)
a,b = map(int,input().split(" "))


def two(n):
    if n % 2 == 0:
        return True
    else:
        return False

def five(n):
    if n%10 == 5:
        return True
    else:
        return False

def three_nine(n):
    if n%3 ==0 and n%9 !=0:
        return True
    else:
        return False

def is_on(a,b):
    n_list =[]
    for i in range(a,b+1):
        if (two(i) == False) and (five(i) == False) and (three_nine(i) == False):
            n_list.append(i)
    print(len(n_list))

is_on(a,b)
a, b, c = map(int, input().split(' '))

alist = [a, b, c]

def cal(a, b, c):
    mi = []
    val = 1
    mi.append(a)
    for i in alist:
        if val == 3:
            break 
        if alist[val] < mi[0]:
            mi[0] = alist[val]
        else:
            pass
        val += 1     
    return mi[0]

print(cal(a, b, c))
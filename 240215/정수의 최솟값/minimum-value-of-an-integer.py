a,b,c= map(int,(input().split(' ')))
alist = []

alist = [a, b, c]

def cal(a,b,c):
    mi = []
    val = 1
    mi.append(a)
    for i in alist:
       if val == 3:
        break 
       if alist[val] < mi[0]:
        mi[0].replace(alist[val])
       else:
        pass
       val += 1     
    print(mi[0])

cal(a,b,c)
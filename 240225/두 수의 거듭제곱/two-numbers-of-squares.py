a,b = map(int,input().split(" "))

def cal(a,b):
    val = 1
    for i in range(0,b):
        val = val*a
    print(val)


cal(a,b)
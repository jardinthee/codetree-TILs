n, m = tuple(map(int,input().split(' ')))

def gong_finder(n,m):
    g_list = []
    for i in range(1,101):
        if (n%i == 0) and (m%i ==0):
            g_list.append(i)
    print(g_list[-1])

gong_finder(n,m)
n,m = map(int,input().split(" "))



def bae(n,m):
    nlist = []
    gong_list = []
    for i in range(1,100):
        nlist.append(n*i)
    for j in range(len(nlist)):
        if nlist[j] % m == 0:
            gong_list.append(nlist[j])
    print(gong_list[0])


bae(n,m)
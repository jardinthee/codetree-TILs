a,b = map(int,input().split())

def sys(n,m):
    if n<m:
        n+=10
        m*=2
        return n,m

    elif n> m:
        n*=2
        m+=10
        return n,m


a,b = sys(a,b)
print(a,b)
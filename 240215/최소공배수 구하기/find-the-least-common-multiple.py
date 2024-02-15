n,m = map(int,(input().split()))

def max_gong(n,m):
    a_list = []
    val = 1
    for i in range(1,101):
        if i > n and i> m:
            break
        
        elif n%i == 0 and m%i ==0:
            a_list.append(i)
    
    for j in range(len(a_list)):
        
        val*= a_list[j]
    if val == 1:
        val = n*m
        
    
    print(val)

max_gong(n,m)
M , D = map(int,input().split())

M_m = [4,6,9,11]
    
def is_(M,D):
    if M > 12 or D>= 32:
        return False
  
    elif M==2 and D >28:
        return False
 
    elif M in M_m and D ==31:
        return False

    else:
        return True

if is_(M,D)== True:
    print("Yes")
else:
    print("No")
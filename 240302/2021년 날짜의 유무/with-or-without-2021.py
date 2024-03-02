M , D = map(int,input().split())


    
def is_(M,D):
    if M > 12 or D > 31:
        return False
  
    elif (M==2) and D >28:
        return False
 
    elif (M ==2,4,6,9,11) and D ==31:
        return False

    else:
        return True

if is_(M,D):
    print("Yes")
else:
    print("No")
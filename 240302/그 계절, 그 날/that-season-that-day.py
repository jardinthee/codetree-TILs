Y , M , D = map(int,input().split())

def is_yoon(Y):
    if Y % 4 == 0 and Y % 100 != 0:
        return True
    elif Y % 4 == 0 and Y%100==0 and Y %400 ==0:
        return True
    else:
        return False

def exist(Y,M,D):
    M_m = [4,6,9,11]
    if M > 12 or D>= 32:
        return False
    elif is_yoon(Y) == True and D==29:
        return True
    
    elif M==2 and D >28:
        return False
 
    elif M in M_m and D ==31:
        return False
    else:
        return True

def season(Y,M,D):
    if exist(Y,M,D) == False:
        print('-1')
    elif exist(Y,M,D):
        if M in (3,4,5):
            print('Spring')
        elif M in (6,7,8):
            print('Summer')
        elif M in (9,10,11):
            print('Fall')
        elif M in (12,1,2):
            print('Winter')

season(Y,M,D)
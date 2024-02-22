n = int(input())

def is_yoon(n):

    if n % 100 ==0 and n % 400 != 0:
        print('false')
        
    elif n % 4 !=0:
        print('false')

    else:
        print('true')

is_yoon(n)
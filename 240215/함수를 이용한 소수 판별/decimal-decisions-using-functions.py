a,b = map(int,input().split())




def is_Prime(N):
    switch = 0

    if N == 1:
        return False


    for n in range(2,N):
        if N % n == 0:
          switch += 1
        
    if switch == 0:
        return True    


def add_all_Primes(a,b):
    val = 0
    for i in range(a,b+1):
        if is_Prime(i):
            val+=i
    print(val)


add_all_Primes(a,b)
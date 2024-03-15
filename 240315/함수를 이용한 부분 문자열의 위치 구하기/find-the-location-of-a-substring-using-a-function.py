N = input()
M = input()

def isin():
    for i in range(len(N)-1):
        if M == N[i:i+len(M)]:
            return i
        else:
            pass
    return -1        
    

print(isin())
N = input()
M = input()

def isin():
    for i in range(len(N)):
        if N[i:i+len(M)] == M:
            return i
        else:
            pass
    return -1

print(isin())
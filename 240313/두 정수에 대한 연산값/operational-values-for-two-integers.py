a,b = map(int, input().split())

def sys(A,B):
    if A > B:
        A += 25
        B*=2
        return A , B

    elif A < B:
        A*=2
        B += 25
        return A,B

a, b = sys(a,b)
print(a,b)
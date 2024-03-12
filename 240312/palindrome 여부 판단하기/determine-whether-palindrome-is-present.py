A = list(input())

def is_pal(N):
    for i in N[::-1]:
        for j in N:
            if i == j:
                return True

if is_pal:
    print("Yes")
else:
    print("No")
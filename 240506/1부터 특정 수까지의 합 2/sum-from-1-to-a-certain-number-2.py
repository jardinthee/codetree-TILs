N = int(input())

def plus(num):
    if num == 1:
        return 1

    return plus(num-1) + num

print(plus(N))
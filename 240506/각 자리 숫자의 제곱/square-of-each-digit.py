N = int(input())

def plus(num):
    if num<10:
        return num**2

    return (plus(num//10) + plus(num%10))

print(plus(N))
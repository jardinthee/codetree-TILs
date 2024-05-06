N = int(input())

def print_(num):
    if num == 0:
        return

    print(num , end = " ")
    print_(num-1)
    print(num , end = " ")

print_(N)
N = int(input())

def star(num):
    if num == 0:
        return

    star(num-1)
    print("*" * num)

star(N)
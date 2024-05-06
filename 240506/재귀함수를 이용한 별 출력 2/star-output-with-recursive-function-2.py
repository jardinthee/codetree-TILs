N = int(input())

def print_star(num):
    if num == 0:
        return

    print("* " * num)
    print_star(num-1)
    print("* " * num)

print_star(N)
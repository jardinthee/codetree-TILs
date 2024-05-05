N = int(input())

def up_num_list(num):
    if num == 0:
        return

    up_num_list(num-1)
    print(num , end = " ")

def down_num_list(num):
    if num == 0:
        return

    print(num, end = " ")
    down_num_list(num-1)


up_num_list(N)
print()
down_num_list(N)
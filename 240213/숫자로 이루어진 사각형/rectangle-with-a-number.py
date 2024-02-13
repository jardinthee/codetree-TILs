I = int(input(''))


def print_square(N):
    val = 1
    for i in range(N):  
        for j in range(N):
            print(val, end=" ")
            val += 1
            if 10 == val:
                val = 1
        print('')    

print_square(I)
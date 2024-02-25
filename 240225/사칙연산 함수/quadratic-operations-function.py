a,o,c = input().split()
a = int(a)
c = int(c)
def cal(a,o,c):
    if o == '+':
        print(f'{a} {o} {c} = {a+c}')
    elif o == '-':
        print(f'{a} {o} {c} = {a-c}')
    elif o == '/':
        print(f'{a} {o} {c} = {a/c.f}')
    elif o == '*':
        print(f'{a} {o} {c} = {a*c}')
    else:
        print('False')


cal(a,o,c)
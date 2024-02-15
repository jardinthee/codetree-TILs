a,b = map(int,input().split(" "))
value = 0

def condition(n):
    num_list = ['3','6','9']
    switch = 0
    str_num = str(n)
    for i in range(len(str_num)):
        if str_num[i] in num_list:
            switch += 1
    if switch != 0:
        return True
        

def machine(n):
    if n % 3 == 0 or condition(n) == True:
        return True

for i in range(a,b+1):
    if machine(i) == True:
        value += 1

print(value)
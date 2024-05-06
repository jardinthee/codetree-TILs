a , b = map(int,input().split())

val = []
str_num = "{:.6f}".format(a / b)

for i in range(2,8):
    val.append(str_num[i])


head = a//b
str_head = str(a//b)+"."

if val[-1] == "0":
    for j in range(len(val)):
        str_head += val[j] 
    str_head += "0"*(20 - len(val))

else:
    for j in range(1,21):
        if j % 6 == 1:
            str_head += val[0]
        elif j % 6 == 2:
            str_head += val[1]
        elif j % 6 == 3:
            str_head += val[2]
        elif j % 6 == 4:
            str_head += val[3]
        elif j % 6 == 5:
            str_head += val[4]
        elif j % 6 == 0:
            str_head += val[5]
print(str_head)
class Info:
    def __init__(self,code,color,second):
        self.code = code
        self.color = color
        self.second = second

a , b, c = tuple(input().split())

A = Info(a,b,c)

print(f"code : {A.code}")
print(f"color : {A.color}")
print(f"second : {A.second}")
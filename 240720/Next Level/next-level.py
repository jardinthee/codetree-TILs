class User_level:
    def __init__(self,Id="codetree",lev=10):
        self.Id = Id
        self.lev = lev



a,b = tuple(input().split())

one = User_level()
two = User_level(a,int(b))

print(f"user {one.Id} lv {one.lev}")
print(f"user {two.Id} lv {two.lev}")
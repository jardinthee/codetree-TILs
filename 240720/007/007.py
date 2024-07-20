class Secret:
    def __init__(self,code,place,time):
        self.code = code
        self.place = place
        self.time = time

code_1 , place_1, time_1 = tuple(input().split())

one = Secret(code_1,place_1,int(time_1))

print(f"secret code : {one.code}")
print(f"meeting point : {one.place}")
print(f"time : {one.time}")
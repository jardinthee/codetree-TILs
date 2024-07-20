class Info:
    def __init__(self,name,code,loc):
        self.name = name
        self.code = code
        self.loc = loc


information = []

n = int(input())
for i in range(n):
    a, b, c = tuple(input().split())
    information.append(Info(a,b,c))

target_idx = 0
for i, ob in enumerate(information):
    if ob.name > information[target_idx].name:
        target_idx = i

# 결과 출력
print(f"name {information[target_idx].name}")
print(f"addr {information[target_idx].code}")
print(f"city {information[target_idx].loc}")
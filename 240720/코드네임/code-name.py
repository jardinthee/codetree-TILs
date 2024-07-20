class Info:
    def __init__(self,code_name="unk",score=0):
        self.code_name = code_name
        self.score = score

agents = []

for _ in range(5):
    code_name , score = tuple(input().split())
    agents.append(Info(code_name,int(score)))

min_idx = 0
for i in range(1,5):
    if agents[min_idx].score > agents[i].score:
        min_idx = i

print(agents[min_idx].code_name, agents[min_idx].score)
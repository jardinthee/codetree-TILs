class Weather:
    def __init__(self,date,day,weather):
        self.date = date
        self.day = day
        self.weather = weather


n = int(input())

w_list = []
r_list = []

for i in range(n):
    date, day, w = tuple(input().split())
    w_list.append(Weather(date,day,w))

for i,ob in enumerate(w_list):
    if ob.weather == "Rain":
        r_list.append(ob)

#rainy day
min_idx = 0
for i,ob in enumerate(r_list):
    if int(ob.date[0:4]) == int(r_list[min_idx].date[0:4]):
        if int(ob.date[5:7]) == int(r_list[min_idx].date[5:7]):
            if int(ob.date[8:10]) == int(r_list[min_idx].date[8:10]):
                min_idx = i
    if int(ob.date[0:4]) == int(r_list[min_idx].date[0:4]):
        if int(ob.date[5:7]) < int(r_list[min_idx].date[5:7]):
            min_idx = i
    if int(ob.date[0:4]) < int(r_list[min_idx].date[0:4]):
        min_idx = i


print(r_list[min_idx].date,r_list[min_idx].day,r_list[min_idx].weather)
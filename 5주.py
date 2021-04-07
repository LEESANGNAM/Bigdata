d3 = {2016:"원숭이",2017:"닭",2018:"개",2019:"돼지",2020:"쥐"}
print(len(d3))

name = "이상남"
birth ="1월16일"
job="학생"
t1 = "name",name
t2 = "birth",birth
t3 = "job",job # 튜플

data = [t1,t2,t3]   # 리스
print(data)

d1_from_list = dict(data) #사전
print(d1_from_list)


d1_other = {"position": "home"}

d1_from_list.update(d1_other)

print(d1_from_list)
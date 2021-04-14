# 집합 만들기


s={1,2,3}
s2={2.5,5,7.5,10,15,20,24}

print(s)
print(s2)
#순서가 존재하기 때문에 인덱싱을 할 수 없다.
#특정한 원소에 접근하려면 리스트 또는 튜플로 변환 한 뒤 인덱싱 한다.
t1_s2 = list(s2)
print(t1_s2[1])

#원소 추가하기

s.add(4)
s.add("python")
print(s)

#교집합

a={1,2,3,4,5}
b={2,4,6,8}
print(a.intersection(b))
print(a&b)

#합집합

print(a.union(b))
print(a|b)

#차집합

print(b.difference(a))
print(a.difference(b))
print(b-a)
print(a-b)

# 집합 크기구하기

ss1={1,2,3}
ss2={2,5,7,10}
ss3=set("Hello")

print(ss1)
print(ss2)
print(ss3)
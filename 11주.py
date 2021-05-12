for i in range(1,10,2):
    print(i)
print("######################")
for i in range(10,0,-1):
    print(i)
print("######################")
t=(1,"python",3.14,-999,False)
for i in t:
    if type(i) == int:
        print(i)

print("######################")
s="Hello, my name is 'Lee, Sang=nam.'"

for c in s:
    if c!=" ":
        print(c,end=" ")
print("######################")
primes = []
for i in range(2, 40):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primes.append(i)
print("2부터 10 사이의 소수는 ",primes,"입니다")

print("######################")

c=[57,-9,3.14,0,-123.45]
#리스트 함축 기법  리스트 이름 = [연상 for 변수 in 기존자료 if 조건문]
d=[x for x in c if x>0]  # c에서 0이 넘는 수만 빼서 d에 저

print(d)
print("######################")
#사전 함축 기법 사전의 이름 = {키 : 값 for 변수 in 기존자료 if 조건문}
a={"a":1, "b":2,"c":3}
b= {v:k for k,v in a.items()} # 키와 값의 위치를 바꾼 후 저장한다.
print(a)
print(b)
print("######################")
c= (1,2,3,4,5)
d={x:x *3 for x in c if x%2 ==1} # 튜플 c에서 홀수만 찾아 키로 할당하고 3을곱해 값으로 할당한다.
print(d)

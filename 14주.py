seasons=["spring","summer","fall","winter","pythong","java"]

for i,s in enumerate(seasons,1):
    print(s,i)

print("===========")

a=[1,2,3,5]
b="abcd"
c=list(zip(a,b))

print(c)
print("===========")

for s,i in zip(seasons,range(0,6)):
    print(s,i+1)
print("===========")
def add(a,b):
    print("입력받은 2개의 숫자는",a,b)
    return a+b
c=add(1,2)
print(c)
print("===========")
def test(a,*b):
    return a-b[-1]
print(test(1,2))
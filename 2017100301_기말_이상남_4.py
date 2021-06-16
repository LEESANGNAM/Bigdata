def calculate_average(a,**d):
    t=a.split('/')
    howlong=len(t)
    name=t[0]
    result=0
    for i in range(1,howlong):
        val=t[i]
        result+=int(val)
    avg=result/i
    d[name]=avg
    return d
d={}
i =1
while i:
    i = int(input("1점수입력 2종료"))
    values = input("성명/점수(들)입력 :")
    d=calculate_average(values,**d)
    print(d)

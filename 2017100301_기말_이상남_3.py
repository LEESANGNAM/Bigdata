


def get_primes(a=10):
    val=[]
    cnt=0
    for i in range(2,a+1):
        chack=True      # 처음 2는 소수 이므로 true 셋팅
        for j in range(2,i):   # 소수를 체크하기위한 i를 제외한수를 모두 나눠
         if i%j==0:     # i를 i로 나누기 전까지 j중에 나누어 떨어지는게 있으면? ex i=10 j=2 나누어 떨어지면?
            chack=False # 소수가 아니다.
            break       # j 반복을 빠져나와서 다시 i를 증가시켜 그다음수를 검사한다.
        if chack is True:   # 만약 브레이크에 걸리지않고 true상태 그대로 내려오면
            val.append(i)        # 소수이므로 리스트에 추가한다.
    return val

values = int(input("정수를 입력하세요. :"))
a= get_primes(values)
print(a)
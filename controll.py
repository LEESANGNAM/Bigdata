# if문    if 조건문 :
#               실행될 문장 (들여쓰기 필수)

if 3.14>2:
    print("3.14가 큰수입니다.")
    print("2가 작은수 입니다.")


a=int(input("정수를 입력하세요 : "))

if a>0:
    print("양수입니다.")
elif a<0:
    print("음수입니다.")
else:
    print("0입니다.")
#윤년 검사 프로그램

year = int(input("연도를 입력하세요  : "))
print("======== 윤년검사 ========")
if ((year % 4 == 0 and year%100!=0)or year%400==0):
    # 입력받은 년도가 (4로나누어떨어지면서 100으로 나누어떨어지지않거나) 400으로 나누어떨어지면 윤년
    print(year,"년은 윤년입니다.")
else:
    print(year,"년은 윤년이 아닙니다.")

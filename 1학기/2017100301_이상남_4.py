# 자동 판매기 프로그램
price = int(input("물건 가격을 입력하세요 : ")) #물건 가격을 int로 받는다.
print("======  입력금액  =======")
price_1000 = int(input("1000원 지폐 개수"))
price_500 = int(input("500원 지폐 개수"))
price_100 = int(input("100원 지폐 개수"))
total_price = (1000*price_1000)+(500*price_500)+(100*price_100) # 투입금액
print("총 투입 금액은 ",total_price,"원 입니다.")
result = total_price - price
# 거스름돈은 투입한 돈을 전부더해 물건가격을 뺀다.
print("=======  거스름돈 ======")
cal_result = result             # 동전갯수에 사용할 변수 : 거스름돈의 값을 넘겨받는다.
num_500=int(cal_result/500)     # 500으로 나눠진 몫을 저장하고
cal_result = cal_result % 500   # 몫을뺀 나머지를 저장해준다.
num_100=int(cal_result/100)     #나머지로 남은 거스름돈을 100으로 나누어 몫을 저장한다.
cal_result = cal_result % 100  #100원의 갯수를 뺀 나머지를 저장해준다.
num_10=int(cal_result/10)
cal_result = cal_result % 10
num_1=int(cal_result/1)                 # 1원의 갯수까지 구하면 출력한다.
print("500원 =",num_500)
print("100원 =",num_100)
print("10원 =",num_10)
print("1원 =",num_1)
print("총 거스름돈은 ",result,"원입니다.")    # 총 거스름돈을 보기쉽게 알려준다.
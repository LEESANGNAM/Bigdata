#평균 계산 프로그램

kor = float(input("국어점수를 입력하세요")) # 사용자로 부터 float타입으로 입력을 받는다.
math =float(input("수학점수를 입력하세요"))
eng = float(input("영어점수를 입력하세요"))

avg = (kor+math+eng)/3  #세개의 값을 입력받아서 avg에 저장한후 출력한다.

print("평균 =",avg) # 형변환없이 출력할 수 있다.
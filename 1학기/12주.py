a = 123
b = "python"

s = '''format값은 {1}가능 {2}또는{0}과 같은 변수에서 대체가능'''.format(a, 3.14, b)

print(s)

# 뒤에있는 c와 인덱스0번 c와는 다르다.
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
c = 123
s = '''format값은 인댁스 대신{c}와같이 가능 {0}또는{1}과 같은 변수에서 대체가능'''.format(c, b, c=456)

print(s)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
# {변수명 또는 인덱스 : 전체 자리수}
s = "내용{0:10}을 전체 10자리로 맞춥니다.".format("python")
print(s)

print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
a = "hello"
# {이미 5자리라서 :3 무시}
s = "내용{:3}와 {:10}의 자리수를 맞춥니다.".format(a, 3.14)
print(s)

print("ㅡㅡㅡ문자열 정렬ㅡㅡㅡㅡㅡ")
s = "오른쪽정렬{0:>10}의 자리수를 맞춥니다.".format("python")
print(s)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
s = "왼쪽정렬{a:<10}의 자리수를 맞춥니다.".format(a=123)
print(s)

print("ㅡㅡㅡ문자열 공백채우기ㅡㅡㅡㅡㅡ")
# {이미 5자리라서 :3 무시}
s = "오른쪽정렬{0:!>10}의 자리수를 맞춥니다. 공백을 ! 로 채우기".format("python")
print(s)
print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
s = "왼쪽정렬{a:!<10}의 자리수를 맞춥니다.".format(a=123)
print(s)

s = "abcdefga"
c= s.replace()
print(c)

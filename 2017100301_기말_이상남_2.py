a=["python","프로그래밍","hi","컴퓨터","data","big","시험","test","연성대학교"]
b=[]
for i in a:
    if len(i)>=3:
        change=i[-1:-7:-1] #거꾸로 인덱싱해서 변수에 저장.
        b.append(change)  #해당 변수를 새로운b리스트의 끝쪽에 추가.
print(b)
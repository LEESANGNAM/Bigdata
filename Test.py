student = {}
i=1;
while i:
    i=int(input("1.학생정보 추가 2.학생정보 수정 3 학생정보 삭제 4.학생정보 하나출력 5.학생정보 모두출력 6.종료"))
    if i==6:
        print("종료합니다.")
        break
    elif i==1:
        stuNum = int(input("학번을 입력해주세요 :"))
        name = input("학생의 이름을 입력해주세요 :")
        dept = input("학생의 학과를 입력해주세요 :")
        rank = input("학생의 성적을 입력해주세요 :")
        if stuNum in student.keys():
            print("이미 있는 학생입니다.")
        else:
            stuInfo = {"이름":name, "학과" : dept, "성적":rank}
            student[stuNum]=stuInfo
    elif i==2:
        stuNum = int(input("수정할 학생의 학번을 입력해주세요 :"))
        while i:
            if stuNum not in student.keys():
                print("학생의 정보가 없습니다. 학번을 다시 입력해주세요.")
                stuNum = int(input("수정할 학생의 학번을 입력해주세요 :"))
            else:
                print("어떤 정보를 바꾸시겠습니까?")
                i = int(input("1.이름 2.학과 3.성적"))
                if i==1:
                    name = input("학생의 이름을 수정해주세요 :")
                    student[stuNum]["이름"]=name
                    break
                elif i == 2:
                    dept = input("학생의 학과를 수정해주세요 :")
                    student[stuNum]["학과"] = dept
                    break
                elif i == 3:
                    rank = input("학생의 성적을 수정해주세요 :")
                    student[stuNum]["성적"] = rank
                    break
    elif i==3:
        stuNum = int(input("삭제할 학생의 학번을 입력해주세요 :"))
        while i:
            if stuNum not in student.keys():
                print("학생의 정보가 없습니다. 학번을 다시 입력해주세요.")
                stuNum = int(input("삭제할 학생의 학번을 입력해주세요 :"))
            else:
                del student[stuNum]
                break
    elif i==4:
        stuNum = int(input("출력할 학생의 학번을 입력해주세요 :"))
        while i:
            if stuNum not in student.keys():
                print("학생의 정보가 없습니다. 학번을 다시 입력해주세요.")
                stuNum = int(input("수정할 학생의 학번을 입력해주세요 :"))
            else:
                print(student[stuNum])
                break
    elif i==5:
        print(student)

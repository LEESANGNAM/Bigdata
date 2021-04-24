#자료비교 프로그램
list1 = []  #사용자로 부터 입력받을 자료를 빈 리스트로 선언.
list2 = []
i=1         #사용자가 입력하때 프로그램을 종료하기 위하여 루프를 들어가기위해 1셋팅
while i:    #값이 들어있을땐 참 이므로 무한 루프
    i = int(input("1.자료1번 값 넣기 2. 자료2번 값넣기 3.자료 출력 4.값비교 5.종료"))
    if i==5:                # 종료를 먼저 잡아내서 종료 출력하고 종료
        print("종료합니다.")
        break;
    elif i==1:              # 사용자가 입력한 값이 1일경우
        val1=int(input("자료1의 값을 입력하세요 : "))     #val1에 자료1의값을 int로 입력받아서
        list1.append(val1)                          # list1의 맨끝에 넣어준다.
    elif i==2:
        val2=int(input("자료2의 값을 입력하세요 : "))
        list2.append(val2)                          #위와 동일하게 list2에 넣어준다.
    elif i==3:
        print("자료1 : ",list1)                      #사용자가 넣은 자료가 궁금할 경우 자료 내용을 출력한다.
        print("자료2 : ",list2)
    elif i==4:
        if not list1 and not list2:             # list1과 list2가 비어있을경우 비교하지않고 비어있다고 출력한다.
            print("두 자료의 값이 비어있습니다.")
        else:                                   # 비어있지않을경우
            if set(list1)==set(list2):             # list1 과 2 를 집합으로 바꾸어 중복값을 제거한 후 비교한다.
                print("2개의 자료구조에 있는 값들이 모두 동일합니다.")
            else:
                print("2개의 자료구조에는 다른 값이 들어있습니다.")


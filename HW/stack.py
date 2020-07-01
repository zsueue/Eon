print("==========메뉴==========\npush:1\npop:2\nshow:3\n종료하려면 1, 2, 3 이외의 수를 입력하세요.")

stack = []

while True:
    menu_num = int(input("메뉴를 선택하세요.: "))

    if menu_num == 1:
        push_num = int(input("수를 입력하세요.: "))
        stack.append(push_num)
    elif menu_num == 2:
        if len(stack) == 0:
            print("스택 안에 데이터가 없습니다. push하여 수를 입력하세요.")
        else:
            stack.pop()
    elif menu_num == 3:
        print(stack)
    else:
        print("==========스택 프로그램을 종료합니다.==========")
        break
import os
import sys
folder = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(folder,'input.txt')

class book:
    def __init__(self, data):
        self.data = data

    def addBook(self):
        f = open("input.txt",'a')
        data = input("추가할 도서명, 저자, 출판연도, 출판사명, 장르를 입력하세요.:")
        f.write(data)
        f.close()

    def searchBook(self):
        import string
        f = open("input.txt", 'a')
        lines = [] #list

        for paragraph in f:
            lines = str.split(paragraph, '.')
            for each_line in lines:
                get = input("검색할 도서의 도서명, 저자, 출판연도, 출판사명, 장르 중 하나를 입력하세요.:")
                if each_line.find(get)>0:
                    print(each_line)
                else:
                    pass
        f.close()

    def modifyBook(self):
        f = open('input.txt', 'r')
        filedata = f.read()
        f.close()

        old = input("수정할 단어를 입력하세요.:")
        new = input("새로운 단어를 입력하세요.:")
        newdata = filedata.replace(old, new)

        f = open('input.txt', 'w')
        f.write(newdata)
        f.close()

    def deleteBook(self):
        with open("input.txt", "r") as f:
            lines = f.readlines()
        with open("input.txt", "w") as f:
            for line in lines:
                delete = input("삭제할 도서의 도서명을 입력하세요.:")
                if line.strip("\n") != delete():
                    f.write(line)

    def showList(self):
        # readline_all.py
        f = open("input.txt", 'r')
        while True:
            line = f.readline()
            if not line: 
                break
            print(line)
        f.close()

    def exitBook(self):
        sys.exit()

    def main():            
        print(""" ======LIBRARY MENU=======
            1. 추가
            2. 검색
            3. 정보 수정
            4. 삭제
            5. 목록 출력
            6. 저장
            7. 프로그램 종료
            """)
        choice=int(input("Enter Choice:"))
        if choice == 1:
            self.addBook()
        elif choice == 2:
            self.searchBook()
        elif choice == 3:
            self.modifyBook()
        elif choice == 4:
            self.deleteBook()
        elif choice == 5:
            self.showList()
        elif choice == 7:
            self.exitBook()                  
    main()



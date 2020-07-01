import os
import sys

class BookDB:
    def __init__(self):
        self.bookDataBase = None
        self.loadData() #불러오고
        self.start() #실행

    def loadData(self): #파일 불러오기
        This_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(This_folder, 'input.txt')
        f = open(my_file, 'r')
        test = f.readlines()
        lines = []
        for i in range(len(test)): #한 줄씩 \n
            lines.append(test[i].split())
        self.bookDataBase = lines #list 형태임

    def addDB(self):
        addData = str(input("추가할 도서의 도서명, 저자, 출판연도, 출판사명, 장르를 입력하세요.:")).split()
        self.bookDataBase.append(addData)

    def searchBook(self): 
        searchData = str(input("검색할 도서의 도서명, 저자, 출판연도, 출판사명, 장르 중 하나를 입력하세요.:"))
        for i in range(0, len(self.bookDataBase)):
            if searchData in self.bookDataBase[i]:
                print(self.bookDataBase[i])

    def modifyDB(self):
        old = str(input("수정할 도서의 도서명, 저자, 출판연도, 출판사명, 장르를 입력하세요.:")).split()
        new = str(input("새로운 도서의 도서명, 저자, 출판연도, 출판사명, 장르를 입력하세요.:")).split()
        for old in self.bookDataBase:
            self.bookDataBase.remove(old)
            self.bookDataBase.append(new)

    def deleteDB(self):
        deleteData = str(input("삭제할 도서의 도서명을 입력하세요.:"))
        for i in range(len(self.bookDataBase)):
            if deleteData == self.bookDataBase[i][0]:
                del self.bookDataBase[i]
                break

    def showDB(self): 
        for i in range(len(self.bookDataBase)):
            print(self.bookDataBase[i])

    def saveDB(self): #loadData() 그대로 복붙하고 r>w바꾸면 되는지?
        
        This_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(This_folder, 'input.txt')
        newfile = open(my_file, 'w')
        for k in range(len(self.bookDataBase)):
            newfile.writelines(' '.join(self.bookDataBase[k]))
            newfile.writelines('\n')
        newfile.close()

    def start(self):
        while(True):
            print("=======MENU=======")
            print("""1. 도서 추가
            2. 도서 검색
            3. 도서 정보 수정
            4. 도서 삭제
            5. 도서 목록 출력
            6. 저장
            7. 나가기
            =====================
            """)
        
            selectMenu = int(input("메뉴 선택 1-7:"))
            if (selectMenu == 1):
                self.addDB()
            elif (selectMenu == 2):
                self.searchBook()
            elif (selectMenu == 3):
                self.modifyDB()
            elif (selectMenu == 4):
                self.deleteDB()
            elif (selectMenu == 5):
                self.showDB()
            elif (selectMenu == 6):
                self.saveDB()
            elif (selectMenu == 7):
                print("프로그램 종료")
                sys.exit()
            else:
                print("1-7사이의 값을 입력해주세요.")

            
Book = BookDB()
Book.loadData()
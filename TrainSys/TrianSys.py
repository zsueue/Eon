import os
import sys
import copy

class TrainDB:
    def __init__(self):
        self.trainDataBase = None
        self.loadData() #불러오고
        self.start() #실행
        self.reservationList = None

    def loadData(self): #파일 불러오기
        This_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(This_folder, 'TrainList.txt')
        f = open(my_file, 'r')
        test = f.readlines()
        lines = []
        for i in range(len(test)):
            lines.append(test[i].split())
        lines.pop(0)
        self.trainDataBase = lines #list

    def searchTrain(self):
        copyDB = copy.deepcopy(self.trainDataBase)
        searchtrain = input("출발시간(08:30), 출발역, 도착역, 열차종류를 입력하세요.:").split()
        for i in range(len(copyDB)):
            if searchtrain[1] != copyDB[i][1]:
                copyDB[i] = [0, 0, 0, 0, 0, 0]
            if searchtrain[2] != copyDB[i][3]:
                copyDB[i] = [0, 0, 0, 0, 0, 0]
            if searchtrain[3] != copyDB[i][4]:
                copyDB[i] = [0, 0, 0, 0, 0, 0]

        # if searchtrain[1] != copyDB[1]: #다르면 copyDB = 0으로
        #     copyDB = [0, 0, 0, 0, 0, 0]
        # elif searchtrain[2] != copyDB[3]:
        #     copyDB = [0, 0, 0, 0, 0, 0]
        # elif searchtrain[3] != copyDB[4]:
        #     copyDB = [0, 0, 0, 0, 0, 0]
        
        searchtrainSum = int(searchtrain[0][0:2]) * 60 + int(searchtrain[0][3:])
        copyDBSum = []
        realtimeList = [605, 635, 715, 842]
        abs_list = []
        for i in range(len(copyDB)):
            if copyDB[i] != [0, 0, 0, 0, 0, 0]:
                copyDBSum.append(int(copyDB[i][0][0:2]) * 60 + int(copyDB[i][0][3:]))
            else:
                copyDBSum.append(0)
            abs_list.append(abs(searchtrainSum - copyDBSum[i]))
            ind = abs_list.index(min(abs_list))

        print("가장 빠른 열차는")
        print(self.trainDataBase[ind])
        print("입니다.")

        # for i in range(len(copyDB)): #그 실제시간 서치 > 리스트출력 안되나? 이중 for문을 이상하게 쓴 듯
        #     if self.trainDataBase[ind] in self.trainDataBase[i]:
        #         print("가장 빠른 열차는")
        #         print(self.trainDataBase[i])
        #         print("입니다.")
        #         break

        self.reservationList = []
        reservationNum = int(input("해당 기차를 예매하시겠습니까? 예:1 아니오:2"))
        if reservationNum == 1:
            self.reservationList.append(self.trainDataBase[ind])
            if int(self.trainDataBase[ind][5]) == 0:
                    print("매진입니다.")
            else:
                self.trainDataBase[ind][5] = str(int(self.trainDataBase[ind][5]) - 1)
        elif reservationNum == 2:
            print("메뉴로 되돌아갑니다.")

    def showDB(self): 
        for i in range(len(self.trainDataBase)):
            if self.trainDataBase[i][5] == '0':
                print(self.trainDataBase[i][:5], '매진')
            else:
                print(self.trainDataBase[i])

    def ReservationDB(self):
        for i in range(len(self.reservationList)):
            print(self.reservationList[i])

        cancelReservationNum = int(input("예매를 취소하시겠습니까? 예:1 아니오:2"))
        if cancelReservationNum == 1:
            cancelReservationData = input("취소할 기차의 시간, 출발역, 도착역, 열차종류를 입력하세요.").split()

            for i in range(len(self.trainDataBase)):
                if cancelReservationData == self.trainDataBase[i]:
                    self.trainDataBase[i][5] = str(int(self.trainDataBase[i][5]) +1)
                    self.reservationList.remove(self.trainDataBase[i])
                    break
        elif cancelReservationNum == 2:
            print("메뉴로 되돌아갑니다.")

    def start(self):
        while(True):
            print("=======MENU=======")
            print("""1. 빠른 시간 기차 검색 및 예매
            2. 전체 기차 리스트 및 출력
            3. 나의 예매 현황 출력 및 예매 취소
            4. 프로그램 종료
            =====================
            """)
        
            selectMenu = int(input("메뉴 선택 1-4:"))
            if (selectMenu == 1):
                self.searchTrain()
            elif (selectMenu == 2):
                self.showDB()
            elif (selectMenu == 3):
                self.ReservationDB()
            elif (selectMenu == 4):
                print("프로그램 종료")
                sys.exit()
            else:
                print("1-4사이의 값을 입력해주세요.")

Train = TrainDB()
Train.loadData()
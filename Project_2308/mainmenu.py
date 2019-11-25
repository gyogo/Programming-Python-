import sys
from memo import Memo
from dday import Dday
from armyword import Armyword
from Project_2308.discharge import Discharge


class Mainmenu:
    def menu(self):
        print("┌─────────메뉴─────────┐")
        for item in ["0. 메모장", "1. 디데이","2. 군대용어","3. 전역일 계산"]:
            print("      "+item)
        print("└──────────────────────┘")

    def main(self):
        while True:
            self.menu()
            answer = input(">> 원하시는 서비스를 입력해주세요~(exit 입력시 종료합니다)\n")
            if answer == 'exit': #exit 받으면 종료
                sys.exit()
            elif answer=='0': # 메모장 실행
                m=Memo()
                m.memo()
            elif answer=='1': # 디데이 실행
                d=Dday()
                d.dday()
                while True:
                    answer = input(">> 계속 하시겠습니까? (예:y, 아니오:n)\n")
                    if answer.lower() == "y": #대소문자 상관없이
                        d.dday()
                    elif answer.lower() == "n":
                        self.main()
                    else:
                        print("※ 다시 입력해주세요! ※")
                        continue #다시 while문으로

            elif answer=='2': #군대용어 실행
                a=Armyword()
                a.quiz()
                while True:
                    answer = input(">> 계속 하시겠습니까? (예:y, 아니오:n)\n")
                    if answer.lower() == "y":
                        a.quiz()
                    elif answer.lower() == "n":
                        self.main()
                    else:
                        print("※ 다시 입력해주세요! ※")
                        continue

            elif answer=='3': #전역일계산기 실행
                d=Discharge()
                d.discharge()
                while True:
                    answer = input(">> 계속 하시겠습니까? (예:y, 아니오:n)\n")
                    if answer.lower() == "y":
                        d.discharge()
                    elif answer.lower() == "n":
                        self.main()
                    else:
                        print("※ 다시 입력해주세요! ※")
                        continue
            else:
                print("※ 재입력해주세요! ※")
                continue

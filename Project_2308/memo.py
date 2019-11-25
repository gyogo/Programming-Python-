import os
import time


class Memo:
    def menu(self):
        print("┌─────────메모장 서비스─────────┐")
        for item in ["0. 새로만들기", "1. 불러오기"]:
            print("           " + item)
        print("└───────────────────────────────┘")

    def memo(self):
        self.menu()
        answer = input(">> 원하시는 서비스를 입력해주세요~ (exit 입력시 종료합니다)\n")
        if answer=='0':
            while True:

                file = input(">> 파일명을 입력하세요 ex) 냥냥.txt (exit입력시 종료합니다)\n")

                if file == 'exit':  # 반복문을 빠져나오는 조건문

                    print("메모장서비스를 종료합니다.\n")
                    print("※ 첫 메뉴로 돌아갑니다. ※\n")
                    time.sleep(2)
                    break

                elif os.path.exists(file):  # 파일 있으면 에러

                    print("※ 파일이 존재합니다. 다시입력해 주세요! ※\n")

                    continue

                else:  # 파일이 없으면 생성

                    f = open(file, "w",encoding="utf8")

                    string = input(">> 간단한 문장을 넣어주세요\n")

                    f.write(string)

                    f.close()

                    print("파일이 생성되었습니다.\n")
        elif answer=='1':
                while True:

                    file = input("불러올 파일명을 입력하세요 (exit입력시 종료합니다)\n")

                    if file == 'exit':

                        print("메모장서비스를 종료합니다.\n")
                        print("※ 첫 메뉴로 돌아갑니다. ※\n")
                        time.sleep(2)
                        break

                    elif os.path.exists(file):

                        f = open(file, "r",encoding="utf8")
                        text = f.read()
                        print(text)
                        f.close()

                    else:
                        print("※ 해당파일이 존재하지않습니다. 다시입력해 주세요! \n")
                        continue

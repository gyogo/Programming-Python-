import random
import os
class Armyword:

    def clear(self):
        for i in range(100):
            print()

    def quiz(self):
        Quiz = [
            ['병사 개개인이 자신의 생명을 보호하기 위해 총검술 따위로 벌이는 전투', '각개전투'],
            ['부사관을 이르는 말', '갈매기'],
            ['예비군 마크를 속되게 부른 말', '개구기마크'],
            ['콘크리트, 모래, 자갈 등을 섞는 작업','공구리'],
            ['자신의 계급과 이름','관등성명'],
            ['군대에 적응하지 못하는 병사를 통상 지칭하는 말','관심병사'],
            ['군대에서 나오는 햄버거를 이르는 말','군대리아'],
            ['군대에서 하는 축구리그를 이르는 말','군대스리가'],
            ['박격포를 이르는 말','똥포'],
            ['편한 보직을 이야기함','땡보'],
            ['병사들이 간부에게 주는 편지(잘한 사람을 칭찬하기 위해 만들어졌으나 요즘은 불만을 표출하는 수단으로 쓰임)','마음의편지'],
            ['군대 고추장으로 밥을 비벼 먹을 때 사용함','맛다시'],
            ['어떤 일을 담당하는 사람의 직책이나 명함','보직'],
            ['신병 교육대의 약자','신교대'],
            ['사회에서 쓰는 물건','싸제'],
            ['신병을 이르는 말 (비슷한 말로 병아리)','신삥']
        ] #퀴즈들
        for x, y in Quiz:  # 리스트의 가로 한 줄(안쪽 리스트)에서 요소 두 개를 꺼냄
            print("▶",x," : ", y)

        start_key=input(">> 아무 키를 누르시면 퀴즈 시작합니다.\n") #값 넣어지면 시작
        self.clear() #문제 위로 올려버리기
        count=0 #정답갯수
        random_list=random.sample(Quiz,5) #10개 랜덤으로 리스트뽑기
        for i in range(len(random_list)): #길이만큼 범위 (인덱스)
            print(">> 이 뜻을 의미하는 단어를 입력하세요!\n")
            print("문제>> ",random_list[i][0])
            answer=input("입력>> ")
            answer = answer.strip()
            if answer==random_list[i][1]:
                print("★ 정답입니다! ★")
                count+=1
            else:
                print("ご.ご 삐빅 - 정답은 ",random_list[i][1],"입니다!")

        if os.path.exists("score.txt"): #이 파일이 있을까요 없을까요 
            file = open("score.txt", "r", encoding="utf8") #있으면 파일 읽기
            if int(file.read())<count: #기록되어있는 count보다 현재 count가 더 높을시 수정
                file = open("score.txt", "w", encoding="utf8")
                file.write(str(count))
        else:
            file = open("score.txt", "w", encoding="utf8") #파일 없을시에 생성하고 값 써주기
            file.write(str(count))
        print("♥ 총 맞은 개수 : ", count, "개")
        file = open("score.txt", "r", encoding="utf8")
        print("♥ 최고 기록:",file.read(),"개")
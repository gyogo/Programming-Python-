from document import Document
from game import Game
from graphic import Graphic
from computer import Computer
import sys
import os
import time

class Order:
    kinds=["문서용","게임용","그래픽작업용"]
    part_list=["V1","V2","V3","V4","V5","V6"]
    part=0
    add_choice=None
    sum_price=0
    def show_menu(self): #메뉴
        print("********** 메뉴 **********")
        print("0. 문서용, 1.게임용, 2. 그래픽작업용\n")

    def budget(self,price): #예산을 입력받자 show_kinds에서 컴퓨터 기본 가격을 price로 넘겨받는다.
      while(True): 
        global user_bud 
        user_bud = int(input("사용자의 예산을 입력해주세요(*만원 단위*) >> "))
        if user_bud < price: #price에 저장된 기본가격보다 적으면 재입력받자(반복)
          print("기본 가격보다 적습니다.")
          print("재입력해주세요.")
        else: #예산이 기본가격보다 같거나 많으면 주문 시작
          self.order()
          break

    def show_kinds(self): #원하는 컴퓨터의 종류를 입력받고 그 종류의 기본성능들을 COMPUTER로 넘긴다.
        self.show_menu() #메뉴를 보여주자
        global order_num
        order_num=int(input("원하시는 종류를 선택하세요. >> "))
        if order_num == 0: #문서용 컴퓨터를 원할 때
          Document.basic(self) #Document에 있는 기본성능 출력하는 함수basic 불러오기
          Computer.price=Document.price #Computer클래스에 있는 price 변수에 Doument에 들어있는 기본 가격 넣어주기
          Computer.CPU=Document.CPU #Computer클래스에 있는 CPU 변수에 Doument에 들어있는 기본 CPU값 넣어주기
          Computer.GPU=Document.GPU #Computer클래스에 있는 GPU 변수에 Doument에 들어있는 기본 GPU값 넣어주기
          Computer.RAM=Document.RAM #Computer클래스에 있는 RAM 변수에 Doument에 들어있는 기본 RAM값 넣어주기
        elif order_num == 1: # 게임용 컴퓨터를 원할 때
          Game.basic(self) #Game에 있는 기본성능 출력하는 함수basic 불러오기
          Computer.price=Game.price #Computer클래스에 있는 price 변수에 Game에 들어있는 기본 가격 넣어주기
          Computer.CPU=Game.CPU #Computer클래스에 있는 CPU 변수에 Game에 들어있는 기본 CPU값 넣어주기
          Computer.GPU=Game.GPU #Computer클래스에 있는 GPU 변수에 Game에 들어있는 기본 GPU값 넣어주기
          Computer.RAM=Game.RAM #Computer클래스에 있는 RAM 변수에 Game에 들어있는 기본 RAM값 넣어주기
        elif order_num ==2: #그래픽작업용 컴퓨터를 원할 때
          Graphic.basic(self) #Graphic에 있는 기본성능 출력하는 함수basic 불러오기
          Computer.price=Graphic.price #Computer클래스에 있는 price 변수에 Graphic에 들어있는 기본 가격 넣어주기
          Computer.CPU=Graphic.CPU #Computer클래스에 있는 CPU 변수에 Graphic에 들어있는 기본 CPU값 넣어주기
          Computer.GPU=Graphic.GPU #Computer클래스에 있는 GPU 변수에 Graphic에 들어있는 기본 GPU값 넣어주기
          Computer.RAM=Graphic.RAM #Computer클래스에 있는 RAM 변수에 Graphic에 들어있는 기본 RAM값 넣어주기
        else: #0,1,2가 아닌 다른 것을 입력했을 때 다시 입력받자.
          print("잘못된 입력입니다.")
          self.show_kinds() #함수 재실행

        self.budget(Computer.price)#예산을 입력받는 함수인 budget에 위에서 넘겨받은 기본 가격을 넘겨준다.
    
    def order(self):
      global answer
      answer=input("기본으로 주문하시겠습니까? (예:y / 아니오:n / 주문종료 : x) >> ")
      if answer.lower()=='y': #Y으로 입력해도 y으로 받기
        self.sum_check() #바로 돈계산으로 들어가기
      elif answer.lower()=='n': #N으로 입력해도 n으로 받기
        self.replace() #교체하는 함수로 이동
      elif answer.lower()=='x': #X로 입력해도 x로 받기
        print("주문을 종료합니다.")
      else: #다른 입력 값이면 함수 재실행 
        print("잘못된 입력입니다.")
        self.order()

    def replace(self): #교체할 부품을 입력한다
          print("교체하실 부품을 입력하세요. >> ")
          global replace_choice
          replace_choice=int(input("0. CPU, 1. GPU, 2. RAM >> "))
          if(replace_choice==self.add_choice): #위에서 add_choice를 none으로 지정해놨는데 나중에 밑에서 추가교체할 때 replace_choice 값을 add_choice에 넣어줘서 이미 바꾼 부품은 못바꾸게 함
              print("이미 교체하신 부품은 다시 교체하실 수 없습니다.")
              order_end=input("주문을 종료하시겠습니까? (예: y/아니오: n) >> ")
              if(order_end.lower()=='y'):
                print("감사합니다")
              elif(order_end.lower()=='n'):
                self.replace() #함수 재실행

          while(True):
            print("어떤 것으로 교체하시겠습니까?")
            Order.part_menu(self) #각 부품에 맞는 메뉴를 보여주는 part_menu함수 불러오기
            self.part=int(input("입력 >> "))

            if replace_choice==0: #문서용 컴퓨터였을 때
              if(self.part==0): #V1으로 선택했을 때
                print("같은 것으로는 교체할 수 없습니다.")
              else:
                Computer.CPU=self.part_list[self.part] #교체된 부품으로 바꿔주기
                self.sum_check() #계산하는 함수 불러오기
                break
           
            elif replace_choice==1:
              if(self.part==1):
                print("같은 것으로는 교체할 수 없습니다.")
              else:
                Computer.GPU=self.part_list[self.part]
                self.sum_check()
                break

            elif replace_choice==2:
              if(self.part==2):
                print("같은 것으로는 교체할 수 없습니다.")
              else:
                Computer.RAM=self.part_list[self.part]
                self.sum_check()
                break
            else:
              print("잘못된 입력입니다.")

    def part_menu(self): #종류에 맞는 메뉴들을 보여줌
      if(order_num==0): #문서용 컴퓨터일 때
        global part_price
        part_price=[0,10,20,30,40,50] #기본 부품 가격은 0 업그레이드 될 수록 10만원씩 추가 다운그레이드는 -10씩
        print("0. V1 추가금액 : ", part_price[0],"만원 | ", "1. V2 추가금액 : ", part_price[1],"만원 | ", "2. V3 추가금액 : ", part_price[2],"만원")
        print("----------------------------------------------------------------------------------")
        print("3. V4 추가금액 : ", part_price[3],"만원 | ", "4. V5 추가금액 : ", part_price[4],"만원 | ", "5. V6 추가금액 : ", part_price[5],"만원")
      elif(order_num==1):
        part_price=[-10,0,10,20,30,40]
        print("0. V1 추가금액 : ", part_price[0],"만원 | ", "1. V2 추가금액 : ", part_price[1],"만원 | ", "2. V3 추가금액 : ", part_price[2],"만원")
        print("----------------------------------------------------------------------------------")
        print("3. V4 추가금액 : ", part_price[3],"만원 | ", "4. V5 추가금액 : ", part_price[4],"5. 만원 | ", "V6 추가금액 : ", part_price[5],"만원")
      elif(order_num==2):
        part_price=[-20,-10,0,10,20,30]
        print("0. V1 추가금액 : ", part_price[0],"만원 | ", "1. V2 추가금액 : ", part_price[1],"만원 | ", "2. V3 추가금액 : ", part_price[2],"만원")
        print("----------------------------------------------------------------------------------")
        print("3. V4 추가금액 : ", part_price[3],"만원 | ", "4. V5 추가금액 : ", part_price[4],"만원 | ", "5. V6 추가금액 : ", part_price[5],"만원")
    
    def sum_check(self):
      if(self.sum_price!=0): #이미 한번 교체를 했었을 때 (sum에 가격이 있을 때)
        self.sum_price+=part_price[self.part] # 기본가격빼고 계산
      elif(answer.lower()=='y'):#기본으로 주문하려 했었을 때
        self.sum_price=Computer.price #sum_price에 기본가격 넘겨주기 
      else:#처음 교체할 때
        self.sum_price+=part_price[self.part]+Computer.price #각 부품별 가격 + 기본가격 넘겨주기

      if(user_bud<self.sum_price): #사용자의 예산이 총 금액보다 적을 때 
        print("예산 : ",user_bud," | 현재 주문 가격 : ",self.sum_price) #얼마나 초과했는지 비교하라고 보여주기
        print("입력하신 예산을 초과하셨습니다.")
        print("주문을 초기화합니다.")
        time.sleep(1) #재우기
        os.system('cls')
        self.show_kinds() #처음부터 실행
      else:
        self.total() #초과 되지 않았을 때 total로 넘어가기
    def total(self):
      os.system('cls')
      print("주문하신 컴퓨터 종류 :",self.kinds[order_num])
      print("----------------------------------")
      print("** 주문하신 컴퓨터 성능 **")
      print("CPU : ",Computer.CPU)#컴퓨터에 저장해놓은 값들 출력
      print("GPU : ",Computer.GPU)
      print("RAM : ",Computer.RAM)
      print("----------------------------------")
      print("총 가격 : ",self.sum_price," 만원")

      self.add_replace()

    def add_replace(self): #추가로 더 교체하는지 안 하는지
      while(True):
        if(answer.lower()=='n'):#기본으로 주문을 안 했을 때
          add=input("추가로 교체하시겠습니까? (예:y /아니오:n) >> ")
          if(add.lower()=='y'):
            self.add_choice=replace_choice #none값이였던 add_choice에 replace함수에서 입력받은 replace_choice값 넘겨주기
            self.replace() #교체 하는 replace함수로 이동 
          elif(add.lower()=='n'): #추가 교체를 안 한다면, 주문완료하고 종료하기
            print("주문이 완료되었습니다! 오늘도 이용해주셔서 감사합니다.")
            sys.exit()
          else: #y/Y or n/N 이 아닌 다른 입력값을 넣었을 때
            print("잘못된 입력입니다! 다시 입력해주세요.")
        else: #기본으로 주문했을 때
          print("주문이 완료되었습니다! 오늘도 이용해주셔서 감사합니다.")
          sys.exit()

      
      
      

        
        





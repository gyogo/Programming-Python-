#야구게임
#세자리 중복없는 임의의 수 만들기
# 무한 반복 while
#사용자 입력 받기 input()
# strike, ball 판정
#사용자 입력한 것, strike, ball 출력하자 print()
# 임의의 수랑 사용자 입력한게 같으면 HIT!, break if
import random
#l=list(range(1,9+1))
#random.shuffle(l)
#l[:3]   #중복없는 리스트 앞부터 3자리
#a="" 
#for i in l[:3]:
   # a+=str(i)  3개 뽑기 
l=random.sample(range(1,9+1),3)
computer = ''.join(str(i) for i in l)

# computer=str(random.randrange(100,999+1)) 이렇게 하려면 중복된 수를 없애야돼
while(True):
    player=input("숫자 세자리를 맞춰보세요 -> ")
    strike=0
    ball=0
    # strike, ball 판정하자
    for i in range(len(computer)):
        for j in range(len(player)):
            if computer[i] == player[j]:
                if i == j: # 자리가 같을 때
                    strike += 1
                else:
                    ball += 1
                
    print("{}\tstrike:{}\tball:{}".format(player,strike,ball))

    if computer == player:
        print("HIT!")
        break
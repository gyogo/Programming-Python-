import random
# def rolling_dice():
#     n=random.randint(1,6) # 1에서 6까지의 랜덤수 1<=n<=6 range랑은 달라
#     print("6면 주사위 굴린 결과 : ",n)
# def rolling_dice(pip):
#     n=random.randint(1,pip) # 1에서 pip까지의 랜덤수 1<=n<=pip range랑은 달라
#     print(pip, "면 주사위 굴린 결과 : ",n)
def rolling_dice(pip,repeat):
    for r in range(1, repeat+1):
        n=random.randint(1,pip) # 1에서 pip까지의 랜덤수 1<=n<=pip range랑은 달라
        print(pip, "면 주사위 굴린 결과 ",r," : ",n) #r은 몇 번째 반복인지보여줌
    

rolling_dice(6,1)
rolling_dice(6,2)
rolling_dice(12,0)
rolling_dice(20,3)


def star():
    print("*****") #print("*"*5)

star()
star()
star()

print("핱")
print("핱", "읖")
print("핱", "읖", "큷")
print("핱", "읖", "큷","슾")
print("핱", "읖", "큷","슾","별")

# def p(*args):
#     string =""
#     for a in args:
#         string +=a
#     print(string)

def p(space, space_num, *args):
    string =args[0]
    for i in range(1,len(args)):
        string +=(space * space_num)+args[i]
    print(string)

p(",",3,'핱',"읖") 
p("별",2,"읖","큷") 
p('핱',5,"읖","큷","슾") 
p('_',3,"읖","큷","슾",) 

def star2(ch,*nums):
    for i in range(len(nums)):
        print(ch*nums[i])
    #for n in nums:
       # print(ch * n)

star2("♬",3)
star2("♡",1,2,3)

def fn (a,b,c,d,e):
    print(a,b,c,d,e)

fn(1,2,3,4,5)
fn(10,20,30,40,50)
fn(5,6,7,8,9)
fn(a=1,b=2,c=3,d=4,e=5) #확정해서 넣기
fn(e=5,d=4,c=3,b=2,a=1)
fn(1,2,c=3,e=5,d=4)
# fn(d=4,e=5,1,2,3) #얘는 오류

def star3(mark, repeat, space, space_repeat,line):
  for _ in range(line):
    string = (mark * repeat) + (space * space_repeat)+(mark * repeat) # "" * 3 + "_" * 2 + "" * 3 
    print (string)
star3("*",3,"_",2,3)

def hello(msg="안녕하세요"): #위에 얘는 업을때만 넣어줘라
        print(msg+"!")

hello("하이")
hello("hi")
hello()

def hello2(name, msg="안녕하세요"):
        print(name+"님, "+msg+"!")


hello2("박교령","오랜만이에요")
hello2("김선옥")
# hello2() 얘는 오류가 나 name에 기본값이 없어서

def fn2(a, b=[]):
        b.append(a)
        print(b)

fn2(3) # -->[3]
fn2(5) # -->[3,5]
fn2(10) # -->[3,5,10]
fn2(7,[1]) #--> [1,7] 걍 외워~
# fn2(a=7,b=[1]):
#   print ([1].append(7))

def gugudan(dan=2):
  for i in range(1,9+1):
        print(dan,"X","=",dan*i) # ,말고 +는 타입 같은애들끼리 연결해주는 거야.
       # print(ste(dan)+"X"+str(i)+"="+str(dan*i)) 

gugudan(3)
gugudan()

def sum(*numbers):
        sum_value =0
        for number in numbers:
                sum_value +=number
        
        return sum_value

print("1 + 3 = ", sum(1, 3))
print("1 + 3 + 5 + 7= ", sum(1, 3, 5, 7))

def min(*numbers):
       min_value = numbers[0]
       for number in numbers:
               if min_value > number:
                       min_value = number
       return min_value
print("min(3, 6, -2) =", min(3, 6, -2))

def max(*numbers):
        max_value = numbers[0]
        for number in numbers:
                if max_value < number:
                        max_value = number
        return max_value

print("max(8, 1, -1, 12) =", max(8,1,-1,12))

def multi_num(multi, start, end):
        result = []
        for n in range(start, end):
                if n % multi == 0:
                        result.append(n)
        return result

print("multi_num(17,1,200) =", multi_num(17,1,200))
print("multi_num(3,1,100) =", multi_num(3,1,100))

def  min_max(*args):
        min_value = args[0]
        max_value = args[0]
        for a in args:
                if min_value>a:
                        min_value = a
                if max_value < a:
                        max_vlaue = a
        return min_value, max_value

min, max = min max(52,-3,23,89,-21)
print("최솟값:",min,"최댓값:",max)


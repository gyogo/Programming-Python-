from _datetime import datetime

print('현재 날짜 시각 객체 얻기')
today = datetime.now()
print('today = datetime.now() : ', today)
print('년 월 일 : today.year, today.month, today.day ', today.year, today.month, today.day)
print('시 분 초 : today.hour, today.minute, today.second', today.hour, today.minute, today.second)
print('요일 : ', today.weekday()) #0이 월요일임
day= datetime(2019,1,1,0,0,0)
print('day = datetime(2019,1,1,0,0,0) : ', day)
print('2019년부터 지나온 시간 구하기')
print('today = day : ',today - day)

my_birth=datetime(2002,12,29)
print("내가 태어난 요일 : ","월화수목금토일"[my_birth.weekday()])
print("내가 산 나날 : ",today-my_birth)
xmas=datetime(2019,12,25)
print("크리스마스는 며칠 남았지? : D", today-xmas)
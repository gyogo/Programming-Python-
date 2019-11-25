import datetime
class Dday:
    def dday(self):
        try:
            startdday = input(">> 시작기준일을 입력하세요. ex)2019-11-03 \n")
            startyy=int(startdday.split('-')[0])
            startmm=int(startdday.split('-')[1])
            startdd=int(startdday.split('-')[2])
            sd = datetime.date(startyy, startmm, startdd) #시작기준일 설정
            enddday = input(">> 끝기준일을 입력하세요 ex)2020-01-01 \n")
            endyy = int(enddday.split('-')[0])
            endmm = int(enddday.split('-')[1])
            enddd = int(enddday.split('-')[2])
            ed = datetime.date(endyy, endmm, enddd) #끝 기준일 설정
            result=(sd - ed).days #차를 구하고 일수로 바꿈
            if result>0:
                print("♣ 디데이 결과: D+",result)
            if result==0:
                print("♣ 디데이 결과: D-DAY")
            else:
                print("♣ 디데이 결과: D",result)
        except Exception:
            print("※ 재입력해주세요. ※")
            self.dday()

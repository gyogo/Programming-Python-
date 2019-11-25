import datetime
class Discharge:
    def discharge(self):
        print("------군별선택------")
        for item in ["0. 육군/의병", "1.해군","2. 공군","3. 해병"]:
            print(item)
        print("---------------------")
        answer = input("입력>> ")
        if not(answer=='0' or answer=='1' or answer=='2' or answer=='3'):
            print("재입력해주세요.")
            self.discharge()
        try:
            startdday = input("입대일을 입력해주세요. ex)2019-07-29\n")
            startyy = int(startdday.split('-')[0])
            startmm = int(startdday.split('-')[1])
            startdd = int(startdday.split('-')[2])
            sd = datetime.date(startyy, startmm, startdd)
            if answer=='0':
                print(sd + datetime.timedelta(days=573-1)) #-1은 당일날 제외
            elif answer=='1':
                print(sd + datetime.timedelta(days=629 - 1))
            elif answer=='2':
                print(sd + datetime.timedelta(days=670 - 1))
            elif answer=='3':
                print(sd + datetime.timedelta(days=573 - 1))
        except Exception:
            print("재입력해주세요.")
            self.discharge()
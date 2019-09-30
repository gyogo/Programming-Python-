fi = open("test.ama","w", encoding="utf8")
fi.write("아이스아메리카노~~~^-^\t2800\t레귤러\t100%\t50%\t코코펄\n")
fi.write("민트오레오쉐이크~~~^-^\t3500\t점보\t50%\t150%\t타피오카펄\n")
fi.write("민트초코버블티~~~^-^\t3800\t레귤러\t100%\t150%\t타피오카펄\n")
fi.close()

fi = open("test.ama","r",encoding="utf8")
sum=0
while True:
    data = fi.readline()
    if not data: #데이터가 없으면
        break   #멈춰라!
    l = data.split("\t") #탭으로 나눠라 .split()는 화이트스페이스(띄어쓰기,\t,\n)으로 분리 지금은 \t로 명시했으니 \t로만 분리해라!
    sum+=int(l[1])
#data = fi.readline() #.read하면 전체가 나와
#fi.close()
#print(data)
fi.close()
print("주문한 총금액: "+str(sum)+"원")
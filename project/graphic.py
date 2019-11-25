

class Graphic:

    CPU="V3" #그래픽 작업용 컴퓨터의 기본 성능
    GPU="V3"
    RAM="V3"
    price=150
    
    def basic(self): #기본 성능 출력
        print("*** 그래픽작업용 기본 성능 ***")
        print("CPU: ",Graphic.CPU)
        print("GPU: ",Graphic.GPU)
        print("RAM: ",Graphic.RAM)
        print("-----------------------")
        print("기본 가격: ",Graphic.price," 만원")
        print("-----------------------")
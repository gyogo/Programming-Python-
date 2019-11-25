

class Game:

    CPU="V2" #게임용 컴퓨터의 기본 성능
    GPU="V2"
    RAM="V2"
    price=100
    
    def basic(self): #기본 성능 출력
        print("*** 문서용 기본 성능 ***")
        print("CPU: ",Game.CPU)
        print("GPU: ",Game.GPU)
        print("RAM: ",Game.RAM)
        print("-----------------------")
        print("기본 가격: ",Game.price," 만원")
        print("-----------------------")
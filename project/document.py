import computer

class Document:

    CPU="V1" #문서용 컴퓨터의 기본값들
    GPU="V1"
    RAM="V1"
    price=50
    
    def basic(self): #기본 성능 출력
        print("*** 문서용 기본 성능 ***")
        print("CPU: ",Document.CPU)
        print("GPU: ",Document.GPU)
        print("RAM: ",Document.RAM)
        print("-----------------------")
        print("기본 가격: ",Document.price," 만원")
        print("-----------------------")
    
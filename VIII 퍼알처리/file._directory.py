import os
data = os.listdir("c:\\") # : 현재 디렉토리 ..: 상위디렉토리
print(data)
for d in data:
    print(d)
    print("is directory?: "+str(os.path.isdir(d)))
    print("is file?: "+str(os.path.isfile(d)))


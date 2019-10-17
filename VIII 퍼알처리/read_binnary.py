#p245
import array

f=open("data.bin","rb")
data = f.read()
#print(data)
for item in data:
    print(item)
f.close()
f = open("fil.txt","r", encoding="stf8")

text = f.read()
print(text)

f.close()

f = open("fil.txt","r", encoding="stf8")

text0 = f.readlines() #\n까지 읽기
print(text0) #\n

text1 = f.readlines()
print(text1)
text2 = f.readlines()
print(text2)
f.close()
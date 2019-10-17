#p239
import pickle

class Person:
    def __init__(self, name, age):
        self.name= name
        self.age = age

    def __str__(self):
        return("이름 : "+self.name+"\n나이 : "+str(self.age))


p = Person("박교령", 18)
#p240
p1 = Person("이은상",19)
p2 = Person("김재환",24)
p3 = Person("박지민",25)
prople = [p1,p2,p3]
f = open("peopel_data.nin","wb")
pickle.dump(p,f)
pickle.dump(p,f) # p객체를 f파일로 내 맘속에 저장 #이것만 추가 됨
f.close()
for p in peo:
    print(p)
#load
#p247
f = open("person_data.bin","rb")
person1 = pickle.load(f)
f.close()
print(person1)
sun =0
for p in peo:
    sum+=p.age
print(sum)

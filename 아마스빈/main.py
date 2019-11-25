from order import Order
from 아마스빈 import file_manager
#History 있으면 내역 보여주자

data = file_manager.load()
for d in data:
    print(d)
print("----------------------------------------------")

o = Order()
o.order_drink()



#history에 저장하자

file_manager.save(o.order_menu)
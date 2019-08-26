#p149 area_main.py
import area2

area2.print_area(10,20)
area2.print_area(20,30)

for i in range(11,15):
    area2.print_area(i,20)

print("가로 30 세로 10인 삼각형의 넓이는",area2.box_area(width,height))
print(area2.__name__)

for i in range(1,100):

    i=str(i)

    if len(i) ==1: #한자리일때
        if i[0] == "3" or i[0] == "6" or i[0] =="9":
            print("짝")
        else:
            print(i)
    elif len(i) == 2: #두자리일때
        if i[0] == "3" or i[0] == "6" or i[0] == "9":
            if i[1] == "3" or i[1] == "6" or i[1] =="9":
                print("짝짝")
            else:
                print("짝")
        else:
            if i[1] == "3" or i[1] == "6" or i[1] =="9":
                print("짝")
            else:
                print(i)


        

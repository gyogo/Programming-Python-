dan = 2
for dan in range(2,10):
    print("---------------------")
    for i in range(1,10): 
        if i > 7:
            break
        if i%2==0:
            continue
        print(dan," x ",i, " = ",dan*i)
       
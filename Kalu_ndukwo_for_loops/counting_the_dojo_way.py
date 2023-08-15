def counting(y):
    for i in range(1,y+1):
        if i % 10 == 0:
            print('coding Dojo')
        elif i % 5 == 0:
            print('coding ')
        else:
            print(i)
        

counting(100)
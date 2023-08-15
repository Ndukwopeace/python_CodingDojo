odd = []
def sum(x):
    y = 0  ## used to find the sum of each element 
    for i in range (0 ,x+1):
        if i % 2 != 0:
            y = y+ i
            odd.append(y)
            ans = odd[len(odd)-1]
    print(ans)
    

sum(1000)

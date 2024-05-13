def moveZeros(arr:[int]):
    n = len(arr)
    temp = []
    for i in range(n):
        if(arr[i] != 0):
            temp.append(arr[i])

    for i in range(n):
        if(arr[i] == 0):
            temp.append(0)

   
    for j in range(n):
        arr[j] = temp[j]
    
    print(arr)

moveZeros([0,0,34,6,8,0,5,0,6,45,8,0,45])




        


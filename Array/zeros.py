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



#USING TWO POINTER OF ARRAYS
def moveZeroTwoPointer(arr:[int]):

    n = len(arr)
    j = 0
    
    for i in range(n):
        if(arr[i] != 0):
            arr[i], arr[j] = arr[j], arr[i]
            j += 1

    print(arr)

moveZeroTwoPointer([1,2,3,1])
moveZeroTwoPointer([0,0,34,6,8,0,5,0,6,45,8,0,45])
        


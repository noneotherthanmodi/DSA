#ROTATE ARRAY TO THE RIGHT BY K STEPS
def rotate(arr:[int],k:int):
    n = len(arr)
    temp = arr[n-1]
    
    
    for j in range(n-1,0,-1):
        arr[j] = arr[j-1]
        
    arr[0] = temp

    print(arr)

rotate([1,2,3,4,5,6,7],3)


#ROTATE ARRAY TO LEFT 
def rotate_left(arr:[int]):
    temp = arr[0]
    n = len(arr)
    for i in range(1,n):
        arr[i-1] = arr[i]
    
    arr[n-1] = temp
    print(arr)

rotate_left([1,2,3,4,5,6,7])

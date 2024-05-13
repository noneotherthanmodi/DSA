#ROTATE ARRAY TO THE RIGHT BY K STEPS
def rotate_right(arr:[int],k:int):
    n = len(arr)
    k = k % n
    if k ==0:
        return
    temp = []
    for i in range(n-k,n):
        temp.append(arr[i])

    # temp = arr[n-1]
    
    
    for j in range(n-1,k-1,-1):
        arr[j] = arr[j-k]
        
    for i in range(0,k):
        arr[i] = temp[i]
    # arr[0] = temp

    print(arr)
rotate_right([-1],1)
rotate_right([1,2,3,4,5,6,7],3)


#ROTATE ARRAY TO LEFT 
def rotate_left(arr:[int],k:int):
    temp = []
    n = len(arr)
    k = k % n
    if k == 0:
        return


    for i in range(k):
        temp.append(arr[i])
    
    
    for i in range(k,n):
        arr[i-k] = arr[i]
    

    for j in range(n-k,n):
        arr[j] = temp[j-(n-k)]

    
    print(arr)


rotate_left([-1],1)
rotate_left([1,2,3,4,5,6,7],3)


#USING REVERSE FUNCTION TO REDUCE SPACE COMPLEXITY:
def rotate_reversely(arr:[int],k:int):

    n = len(arr)
    k = k % n
    arr.reverse()

    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])


    print(arr)

rotate_reversely([1,2,3,4,5,6,7],4)
    
#MAX SIZE OF AN ARRAY THAT CAN BE DEFINED INSIDE AN INT MAIN FUNC IS 10^6, AND GLOBALLY 10^7

def largest_element(arr:[int],n:int):
    largest = arr[0]
    for i in range(n):
        if (arr[i]>largest):
            largest = arr[i]
    print(largest)
        
        
largest_element([7,2,1,5,2],5) 

#SECOND LARGEST ELEMENT:

def second_largest_element(arr:[int],n:int):
    largest = arr[0]
    for i in range(n):
        if arr[i]>largest:
            largest = arr[i]
    
    second_largest = -1
    for i in range(n):
        if(arr[i]>second_largest and arr[i]!=largest):
            second_largest = arr[i]
        
    print(second_largest)

second_largest_element([7,2,1,5,2],5) 
second_largest_element([642 ,642 ,642, 642, 642, 642 ,642 ,642, 642, 642, 642, 642, 642],13) 


from sys import maxsize
def second_smallest(arr:[int],n:int):
    smallest = arr[0]
    for i in range(n):
        if(arr[i]<=smallest):
            smallest = arr[i]

    second_smallest = maxsize
    for i in range(n):
        if(arr[i]<second_smallest and arr[i]!=smallest):
            second_smallest = arr[i]

    print(second_smallest)

second_smallest([7,2,1,3,5,2],6)


#REMOVE DUPLICATE ELEMENTS FROM AN ARRAY:
def remove_duplicate(arr:[int]):
    arr.sort()

    print(arr)
    n = len(arr)
    i = 0
    for j in range(1,n):
        if(arr[i] != arr[j]):
            arr[i+1] = arr[j]
            i+=1
    del arr[i+1:]
    print(arr)
    print(i+1)


remove_duplicate([5,6,2,2,6,4,5,6,1]) 

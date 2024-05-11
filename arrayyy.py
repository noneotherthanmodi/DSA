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
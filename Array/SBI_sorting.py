from typing import List
#FIND THE SHORTEST ELEMENT AND SWAP IT WITH THE FIRST ELEMENT
def selectionSort(arr: List[int],n: int) -> None: 
    # Write your code here
    
    for i in range(0,n-1):
        min = i

        for j in range(i,n):
            if(arr[j]<arr[min]):
                min = j

        #swap (arr[min] and arr[i])
        temp = arr[min]
        arr[min] = arr[i]
        arr[i] = temp
    return arr


#LOOK FOR i+1 AND IF IT IS BIG, EXCHANGE IT WITH i 
def bubbleSort(arr: List[int], n: int):
    # Your code goes here.
    
    for i in range(n-1,0,-1):
        didSwap = 0
        for j in range(0, i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didSwap = 1
        #for best case scenario: o(n)
        if didSwap == 0:
            break
        # print("swaped")
    return arr


def insertionSort(arr: List[int], n: int) -> List[int]:
    # Write your code here
    for i in range(0,n):
        j = i
        while (j>0 and arr[j-1]>arr[j]):
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
        
    return arr


print(selectionSort([2, 13, 4, 1, 3,6, 28], 7))
print(bubbleSort([2, 13, 4, 1, 3,6, 28], 7))
print(insertionSort([2, 13, 4, 1, 3,6, 28], 7))

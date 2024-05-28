#MERGE SORT - DIVIDE AND MERGE with using low and high  
#TIME - O(nlogn) SPACE - O(n)
def mergeSort(arr:[int], low:int, high:int):
    if low >= high:
        return 
    mid = (low + high) // 2 
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    merge(arr, low, mid, high)
    return arr
    
def merge(arr:[int],low:int,mid:int,high:int):
    temp_arr = []
    right = mid+1
    left = low
    while left<=mid and right<=high:
        if arr[left]<arr[right]:
            temp_arr.append(arr[left])
            left+=1
        else:
            temp_arr.append(arr[right])
            right+=1
    while left<=mid:
        temp_arr.append(arr[left])
        left+=1
    while right<=high:
        temp_arr.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i] = temp_arr[i-low]
    return arr

def input_for_merge_sort():
    arr = [4,7,2,54,76,3]
    n = len(arr)
    print("Given array for merge sort is")
    for i in range(n):
        print(arr[i], end = ' ')
    print("\n")
    mergeSort(arr, 0, n-1)
    print("Sorted array for merge sort is : ")
    for i in range(n):
        print(arr[i], end = ' ')
    print("\n")
input_for_merge_sort()





#QUICK SORT - FIND THE PIVOT ELEMENT, PLACE IT IN CENTRE AND THEN SOLVE LEFT AND RIGHT SIDES
#TIME - O(nlogn) SPACE - O(1)
def partition(arr: [int],low: int,high: int):
    pivot = arr[low]
    i = low
    j = high 
    while(i<j):
        while(arr[low] >= arr[i] and i <= high-1):
            i+=1
        while(arr[low] < arr[j] and j >= low+1):
            j-=1
        if (i<j):
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

def quick_sort(arr: [int],low: int, high: int):
    if(low < high):
        pindex = partition(arr, low, high)
        quick_sort(arr, low, pindex-1)
        quick_sort(arr, pindex+1, high)


def input_for_quick_sort():
    arr = [4,7,2,54,76,3]
    n = len(arr)
    print("Given array for quick sort is")
    for i in range(n):
        print(arr[i], end = ' ')
    print("\n")
    quick_sort(arr, 0, n-1)
    print("Sorted array for quick sort is : ")
    for i in range(n):
        print(arr[i], end = ' ')
    print("\n")
            

input_for_quick_sort()
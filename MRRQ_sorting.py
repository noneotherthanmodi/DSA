#MERGE SORT - DIVIDE AND MERGE with using low and high 
def mergeSort(arr, low, high):
    if low >= high:
        return 
    mid = (low + high) // 2 
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    merge(arr, low, mid, high)
    return arr
    
def merge(arr,low,mid,high):
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

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
for i in range(n):
    print(arr[i], end = ' ')
print("\n")
mergeSort(arr, 0, n-1)
print("Sorted array is : ")
for i in range(n):
    print(arr[i], end = ' ')
print("\n")



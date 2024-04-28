#MERGE SORT - DIVIDE AND MERGE with using low and high 
def mergeSort(arr, low, high):
    if low >= high:
        return 
        mid = (low + high) // 2
        mergeSort(arr, low, mid)
        mergeSort(arr, mid + 1, high)
        merge(arr, low, mid, high)
    return arr
    
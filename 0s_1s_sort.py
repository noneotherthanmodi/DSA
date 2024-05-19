from typing import List 
def sortColors(nums: List[int]) -> None:
    n = len(nums)
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for i in range(n):
        if (nums[i] == 0):
            count_0 += 1
        elif(nums[i] == 1):
            count_1 += 1
        elif(nums[i] == 2):
            count_2 += 1

    
    for j in range(count_0):
        nums[j] = 0

    for j in range(count_0, count_0+count_1):
        nums[j] = 1
    for j in range(count_0+count_1, n):
        nums[j] = 2

    print(nums)

sortColors([2,0,2,1,1,0])




#               0        low-1     low       mid-1         high+1     n-1
#               ^         ^         ^         ^              ^         ^
#               |         |         |         |              |         |
#               0 0 0 0 0 0         1 1 1 1 1 1   unsorted   2 2 2 2 2 2
#                                               ~~~~~~~~~~~~

#DUTCH NATIONAL FLAG ALGORITHM 
# T() = O(N)
# S() = O(1)


def sortColors2(arr: List[int]) -> None:
    n = len(arr)
    low = 0
    mid = 0
    high = n-1

    arr[low] = 0
    arr[mid] = 0
    while (mid <= high):
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1

        elif arr[mid] == 1:
            mid += 1

        elif arr[mid] == 2:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    print(arr)
    return arr 

sortColors2([2,0,2,1,1,0])
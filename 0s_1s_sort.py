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


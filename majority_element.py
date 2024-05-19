from typing import List
from collections import Counter



#MOST OPTIMAL ONE ->
def majorityElement1(nums: List[int]) -> int:
    n = len(nums)

    counter = Counter(nums)
    
    for num, count in counter.items():
        if count > (n//2):
            print(num)

    return -1

majorityElement1([3,2,3])






#MORE OPTIMAL ONE ->  MOORE'S VOTING METHOD

def majorityElement2(nums: List[int]) -> int:
    n = len(nums)
    count = 0
    for i in range(n):
        if count == 0:
            count = 1
            element = nums[i]

        elif nums[i] == element:
            count += 1
        
        else:
            count -= 1


    count1 = 0
    for i in range(n):
        if (nums[i] == element):
            count1 += 1

    if count1 > (n // 2):
        print(element)
        return element


# majorityElement2([3,2,3])






#NOT BETTER ONE -> 
def majorityElement3(nums: List[int]) -> int:
    n = len(nums)
    
    for i in range(len(nums)):
        count = 0
        for j in range(i,n):
            if (nums[i] == nums[j]):
                count += 1 
        
            if (count > (n//2)):
                print(nums[i])



# majorityElement3([3,2,3])
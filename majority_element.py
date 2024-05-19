from typing import List


#NOT BETTER ONE -> 
def majorityElement(nums: List[int]) -> int:
    n = len(nums)
    
    for i in range(len(nums)):
        count = 0
        for j in range(i,n):
            if (nums[i] == nums[j]):
                count += 1 
        
            if (count > (n//2)):
                print(nums[i])



majorityElement([3,2,3])
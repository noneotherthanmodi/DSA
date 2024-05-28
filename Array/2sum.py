from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        rem = target - nums[i]
        for j in range(i+1,n):
            if rem==nums[j]:
                
                a = (i,j)
                print(list(a))
                return list(a)
    

twoSum([3,2,4],6)

def twoSum2(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            
            if(nums[i]+nums[j] == target):
                
                a = (i,j)
                
                print(list(a))
                return list(a)
            
twoSum2([3,2,4],6)
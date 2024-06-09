from typing import List 
def search(nums: List[int], target: int) -> int:
    n = len(nums)
    low = 0
    high = n-1
    
    while(low <= high):
        mid = (low+high)//2

        if nums[mid] == target:
            print(mid)
            break 
        elif nums[mid] > target:
            high = mid-1
        
        else:
            low = mid+1 
        
    return -1

search([-1,0,3,5,9,12],3)


#with recursion:






def search2(nums: List[int], target: int) -> int:
    n = len(nums)

    def bs(nums: List[int],low:int,high:int,target:int):
        if(low>high):
            return -1
        
        mid = (low+high)//2
        
        if(nums[mid] == target):
            print(mid)
            
        elif(nums[mid]>target):
            bs(nums,low,high-1,target)
        else:
            bs(nums,mid+1,high,target)




    bs(nums,0,n-1,target)
    

search2([-1,0,3,5,9,12],3)
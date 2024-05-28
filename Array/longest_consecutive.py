#find the longest consecutive in an array:
from typing import List 
import sys
int_max = sys.maxsize
int_min = -int_max - 1

def longestConsecutive(nums: List[int]) -> int:
    nums.sort()
    
    longest = 1
    count = 0
    smallest = float('-inf')


    n = len(nums)
    if n == 0:
        return 0

    

    for i in range(n):
        if (nums[i] - 1 == smallest):
            count += 1
            smallest = nums[i]

        elif (nums[i] != smallest):
            count = 1
            smallest = nums[i]
        
        

        longest = max(longest,count)
    

    print(longest)

longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3])



def longestConsecutive2(nums: List[int]) -> int:
    st = set()
    
    n = len(nums)
    if n == 0:
        return 0 
    
    longest = 1
    

    for i in range(n):
        st.add(nums[i])

    for it in st:
        if it-1 not in st:
            count = 1

            while it+1 in st:
                count += 1
                it += 1
            
            longest = max(longest,count)
    
    print(longest)


longestConsecutive2([0,3,7,2,5,8,4,6,0,1])
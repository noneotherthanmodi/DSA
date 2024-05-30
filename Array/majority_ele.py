from typing import List 
def majorityElement(nums: List[int]) -> List[int]:
    
    ans = []
    n = len(nums)
    for i in range(n):
        if len(ans) == 0 or ans[0] != nums[i]:
            count = 0
            for j in range(i,n):
                if nums[i] == nums[j]:
                    count += 1

                if count > (n//3):
                    ans.append(nums[i])
        if len(ans) == 2:
            break

    print(ans)

majorityElement([3,2,3])


#better:
from collections import Counter
def majorityElement(nums: List[int]) -> List[int]:
    track = 0
    n = len(nums)
    ele = Counter(nums)
    ans = []
    
    for num,count in ele.items():
        if count> (n//3):
            ans.append(num)
            print(ans)

majorityElement([3,2,3])
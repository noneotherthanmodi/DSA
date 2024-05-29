from typing import List     
def subarraySum(nums: List[int], k: int) -> int:
    n = len(nums)
    count = 0
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum += nums[j]

            if sum == k:
                count += 1
            
    print(count)

subarraySum([1,2,3],3)




#OPTIMAL ONE:  T() : O(n*logn), S(): O(n)
from collections import defaultdict
def subarraySum2(nums: List[int], k: int) -> int:
    n = len(nums)
    mpp = defaultdict(int)
    preSum = 0
    count = 0

    mpp[0] = 1
    for i in range(n):
        preSum += nums[i]

        remove = preSum - k

        count += mpp[remove]

        mpp[preSum] += 1

    print(count)

subarraySum2([1,2,3],3)
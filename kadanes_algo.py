#MAXIMUM SUBARRAY SUM - KADANE'S ALGORITHM
from typing import List
import sys 
max_int = sys.maxsize
min_int = -max_int - 1




















#NOT AN OPTIMAL ONE ->
def maxSubArray(nums: List[int]) -> int:
    maxi = min_int
    n = len(nums)
    for i in range(len(nums)):
        sum = 0
        for j in range(i,n):
            sum += nums[j]

            maxi = max(sum,maxi)

    print(maxi)

maxSubArray([5,4,-1,7,8])
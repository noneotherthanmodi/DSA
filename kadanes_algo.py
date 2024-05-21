#MAXIMUM SUBARRAY SUM - KADANE'S ALGORITHM
from typing import List
import sys 
max_int = sys.maxsize
min_int = -max_int - 1


#OPTIMAL SOLUTION ->
def maxSubArray1(nums: List[int]) -> int:
    n = len(nums)
    sum = 0
    maxi = min_int
    for i in range(n):
        sum += nums[i]

        if sum > maxi:
            maxi = sum

        if sum < 0:
            sum = 0
            

        


    print(maxi)




maxSubArray1([-2,1,-3,4,-1,2,1,-5,4])







#NOT AN OPTIMAL ONE ->
def maxSubArray2(nums: List[int]) -> int:
    maxi = min_int
    n = len(nums)
    for i in range(len(nums)):
        sum = 0
        for j in range(i,n):
            sum += nums[j]

            maxi = max(sum,maxi)

    print(maxi)

maxSubArray2([-1])
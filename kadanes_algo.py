#MAXIMUM SUBARRAY SUM - KADANE'S ALGORITHM    T() : O(N),  S() : O(1)  
from typing import List
import sys 
max_int = sys.maxsize
min_int = -max_int - 1


#OPTIMAL SOLUTION ->
def maxSubArray1(nums: List[int]) -> int:
    n = len(nums)
    sum = 0
    maxi = min_int
    for i in range(n):                      #TO KEEP THE TRACK OF INDEX OF SUBARRAYS:
                                            #if (sum == 0): start = i
        sum += nums[i]                          


        if sum > maxi:
            maxi = sum
                                            #ansStart = start, ansEnd = i
        if sum < 0:
            sum = 0
            

        


    print(maxi)




 
maxSubArray1([-7 ,-8, -16, -4, -8, -5, -7, -11, -10, -12, -4, -6, -4, -16, -10])







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

maxSubArray2([-7 ,-8, -16, -4, -8, -5, -7, -11, -10, -12, -4, -6, -4, -16, -10])
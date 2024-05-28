#VERY IMPORTANT
#less optimal ->
from typing import List
def longestSubarrayWithSumK(a: List[int], k: int) -> int:
    # Write your code here
    n = len(a)
    
    maxlen = 0
    for i in range(len(a)):
        sum = 0
        for j in range(i,n):
            sum += a[j]
    
            if sum == k:
                maxlen = max(maxlen,j-i+1)
            
    return maxlen 


#BEST OPTIMIZED : 
def longestSubarrayWithSumKk(a: List[int], k: int) -> int:
    # Write your code here
    preSumMap = {}
    maxlen = 0
    Sum = 0
    n = len(a)
    for i in range(n):
            
        Sum += a[i]
                
        if Sum==k:
            maxlen = max(maxlen,i+1)
                    
                    
        rem = Sum-k
            
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxlen = max(maxlen,length)
                
        if Sum not in preSumMap:
            preSumMap[Sum] = i
                
    return maxlen

print(longestSubarrayWithSumKk([2, 3, 5, 1, 9],10))
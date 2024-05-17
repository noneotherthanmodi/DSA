#VERY IMPORTANT
#less optimal ->
def longestSubarrayWithSumK(a: [int], k: int) -> int:
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

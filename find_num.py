from typing import List
def missingNumber(a : List[int], N : int) -> int:
    # Write your code here.
    
    for i in range(1,N+1):
        flag = 0
        for j in range(len(a)):
            if(a[j] == i):
                flag = 1
                break
            
        if (flag==0):
            return i
   
    return -1

    

print(missingNumber([1,2,4,5],5))

def missingNum(a:List[int],n:int) -> int:
    sum = n*(n+1)//2
    s = 0
    for i in range(n-1):
        s += a[i]

    val = sum-s
    # print(val)

missingNum([1,2,4,5],5)


#FIND NUMBER THAT APPEARS JUST ONCE:
def singleNumber(nums: List[int]) -> int:
    for num in nums:
        number = num
        count = 0
        for other_num in nums:
            if other_num == number:
                count += 1
        if count == 1:
            return num
    

print(singleNumber(nums=[4,1,2,1,2]))
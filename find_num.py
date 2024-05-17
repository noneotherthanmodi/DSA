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
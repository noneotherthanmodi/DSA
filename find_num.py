from typing import List
def missingNumber(a : List[int], N : int) -> int:
    # Write your code here.
    flag = 0
    for i in range(1,N):
        for j in range(0,N-1):
            if(a[j] == i):
                flag = 1
                break
            
        if (flag==0):
            return i

    print(i)

missingNumber([1,2,4,5],5)

def missingNum(a:List[int],n:int) -> int:
    sum = n*(n+1)//2
    s = 0
    for i in range(n-1):
        s += a[i]

    val = sum-s
    print(val)

missingNum([1,2,4,5],5)
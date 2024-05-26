from typing import List
def alternateNumbers(a : List[int]) -> List[int]:
    # Write your code here.
    pos = []
    neg = []
    n = len(a)
    for i in range(n):
        if a[i]>0:
            pos.append(a[i])

        else:
            neg.append(a[i])

    
    for i in range(n//2):
        a[2*i] = pos[i]
        a[2*i + 1] = neg[i]

        
    print(a)

alternateNumbers([1, 2, -3, -1, -2, 3])

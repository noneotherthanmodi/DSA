from typing import List

#this includes the positives and negatives of not same length -> 
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

    if((len(pos)) > (len(neg))):
        for i in range(len(neg)):
            a[2*i] = pos[i]
            a[2*i + 1] = neg[i]
        
        index = len(neg) * 2
        for i in range(len(neg), len(pos)):
            a[index] = pos[i]
            index += 1


    else:
        for i in range(len(pos)):
            a[2*i] = pos[i]
            a[2*i + 1] = neg[i]
        
        index = len(pos) * 2
        for i in range(len(pos), len(neg)):
            a[index] = neg[i]
            index += 1 
    
    

        
    print(a)

alternateNumbers([1, 2, -3, -1, -2, 3, -4, -5, -6])





def alternateNumbers(a : List[int]) -> List[int]:
    # Write your code here.
    pos = 0
    neg = 1
    n = len(a) 
    ans = [0] * n
    
    for i in range(n):
        if a[i]>0:
            ans[pos] = a[i]
            pos += 2
            

        else:
            ans[neg] = a[i]
            neg += 2


    
    

        
    print(ans)

alternateNumbers([1, 2, -3, -1, -2, 3])
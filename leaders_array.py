def leaders(A, N):
    ans = []
    for i in range(N):
        leader = True
        for j in range(i+1,N):
            if A[j] > A[i]:
                leader = False 
                break 

        if leader:
            ans.append(A[i])
        
    print(ans)

leaders([16,17,4,3,5,2],6)


import sys
def leaders2(a,n):
    int_max = sys.maxsize
    int_min = -int_max -1 
    
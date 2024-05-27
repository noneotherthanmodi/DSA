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

# leaders([16,17,4,3,5,2],6)



def leaders2(a,n):
    ans = []
    max_ele = a[n-1]
    ans.append(max_ele)
    
    for i in range(n-2,-1,-1):
        if a[i] > max_ele:
            ans.append(a[i])
            max_ele = a[i]
        
    
    print(ans)

leaders2([16,17,4,3,5,2],6)
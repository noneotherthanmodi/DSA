def union_of_array(arr1,arr2,m,n):
    st = set()
    union = []
    for num in arr1:
        st.add(num)

    for num in arr2:
        st.add(num)

    for s in st:
        union.append(s)

    union.sort()

    print(union)
union_of_array([1,2,3,4,6,7,7,6],[3,4,5,4,1,2,3,9],8,8) 


#USING TWO POINTER 
def union_using_two_pointer(arr1,arr2):
    m = len(arr1)
    n = len(arr2)

    i = 0
    j = 0
    union_array = []
    while (i<m and j<n):
        if(arr1[i] <= arr2[j]):
            if(len(union_array) == 0 or union_array[-1] != arr1[i]):
                union_array.append(arr1[i])
            i += 1

        else:
            if(len(union_array)==0 or union_array[-1] != arr2[j]):
                union_array.append(arr2[j])
            j+=1


    while(j<n):
        if(len(union_array) == 0 or union_array[-1]!=arr2[j]):
            union_array.append(arr2[j])
        j += 1

    while(i<m):
        if (len(union_array) == 0 or union_array[-1] != arr1[i]):
            union_array.append(arr1[i])

        i += 1

    print(union_array)

union_using_two_pointer([1,2,3,4,6,7,7,6],[3,4,5,4,1,2,3,9]) 


def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    
    n = len(a)
    m = len(b)

    unionArray = []
    i = 0
    j = 0

    while(i<n and j<m):
        if (a[i]<=b[j]):
            if (len(unionArray) ==0 or unionArray[-1] != a[i]):
                unionArray.append(a[i])
            i += 1
        else:    
            if(len(unionArray) == 0 or unionArray[-1] != b[j]):
                unionArray.append(b[j])
            j += 1

    while(j<m):
        if(len(unionArray) == 0 or unionArray[-1] != b[j]):
            unionArray.append(b[j])
        j+=1
    while(i<n):
        if(len(unionArray) == 0 or unionArray[-1] != a[i]):
            unionArray.append(a[i])
        i += 1

    print(unionArray)
    return unionArray

sortedArray([1,2,3,4,6,7,7,6],[3,4,5,4,1,2,3,9]) 

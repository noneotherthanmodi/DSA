def union_of_array(arr1,arr2):
    m = len(arr1)
    n = len(arr2)
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



arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [1, 2, 3, 4, 4, 5, 11, 12]


union_of_array(arr1,arr2)
union_using_two_pointer(arr1,arr2)

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

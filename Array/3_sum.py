from typing import List 

#brute solution: 
def threeSum(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    st = set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k] == 0:
                    temp = [nums[i],nums[j],nums[k]]
                    temp.sort()
                    st.add(tuple(temp))
                
    ans = [list(item) for item in st]

    print(ans)

threeSum([-1, 0, 1, 2, -1, -4])



#better with T(): O(N^2 * log(no. of unique triplets)), where N = size of the array.
def threeSum2(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    
    st = set()
    for i in range(n):
        hashnet = set()

        for j in range(i+1,n):
            third = -(nums[i] + nums[j])

            if third in hashnet:
                temp = [nums[i],nums[j],third]
                temp.sort()
                st.add(tuple(temp))

            hashnet.add(nums[j])
             
                
    ans = list(st)

    print(ans)


threeSum2([-1, 0, 1, 2, -1, -4])
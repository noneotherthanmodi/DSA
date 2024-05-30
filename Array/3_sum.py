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
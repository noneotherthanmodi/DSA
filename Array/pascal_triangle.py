from typing import List 

#                                                    R-1
# i) to find the element at Rth row and Cth coloumn:   C           = nCr - > (r-1)C(c-1)
#                                                       C-1

def nCr(n:int, r: int):            #take r-1 and c-1 for pascal's triangle
    res = 1
    for i in range(r):
        res = res * (n-i)
        res /= (i+1)
    print(res)




def generate(numRows: int) -> List[List[int]]:
    for i in range(numRows):
        pass 
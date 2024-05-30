from typing import List 

#                                                    R-1
# i) to find the element at Rth row and Cth coloumn:   C           = nCr - > (r-1)C(c-1)
#                                                       C-1

def nCr(n:int, r: int):            #take r-1 and c-1 for pascal's triangle
    res = 1
    for i in range(r):
        res = res * (n-i)
        res = res // (i+1)
    return(res)


def find_nth_ele(r,c):
    element = nCr(r-1,c-1)
    print (element)
find_nth_ele(5,3)



def print_entire_row(n):
    for c in range(1,n+1):
        print(nCr(n-1,c-1),end = "")

print_entire_row(2)




def generate(numRows: int) -> List[List[int]]:
    ans = 1
    if numRows == 1:
        return 1
    
        


# generate(4)
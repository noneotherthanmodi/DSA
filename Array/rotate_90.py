from typing import List 
import numpy as np
def rotate(matrix: List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])
    ans = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            ans[j][(m-1)-i] = matrix[i][j]

    for i in range(m):
        for j in range(n):
            matrix[i][j] = ans[i][j]
    
    print(matrix)

# rotate([[1,2,3],[4,5,6],[7,8,9]])

#REPRESENTATION FOR ABOVE CODE:
#  i  j      j (m-1)-i       i  j   j  (m-1)-i
# [0][0] -> [0][3]          [1][0]->[0][2]
# [0][1] -> [1][3]          [1][1]->[1][2]
# [0][2] -> [2][3]          [1][2]->[2][2]
# [0][3] -> [3][3]          [1][3]->[3][2]






def rotate2(matrix: List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(m):
        matrix[i] = matrix[i][::-1]

    print(matrix)


rotate2([[1,2,3],[4,5,6],[7,8,9]])
from typing import List 

#TIME -> O(2*m*n)
#SPACE -> O(m)+O(n)
def setZeroes(matrix: List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])
    row = [0] * m
    col = [0] * n

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1



    for i in range(m):
        for j in range(n):
            if ((row[i] or col[j]) == 1):
                matrix[i][j] = 0

    print(matrix)


setZeroes([[1,1,1],[1,0,1],[1,1,1]])










#TIME COMPLEXITY FOR THIS PARTICULAR SITUATION: (m*n)*(m+n) + (m*n) -> somewhere around: {O(n)^3}
def setZeroes2(matrix: List[List[int]]) -> None:
    m = len(matrix)
    n = len(matrix[0])

    def rowZero(i):
        for j in range(m):
            if matrix[i][j] != 0:
                matrix[i][j] = -1 

    def rowCol(j):
        for i in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] = -1


    for i in range(m):
        for j in range(n):
            if (matrix[i][j] == 0):
                rowZero(i) 
                rowCol(j) 

    for i in range(m):
        for j in range(n):
            if (matrix[i][j] == -1):
                matrix[i][j] = 0

    

    print(matrix) 

setZeroes2([[1,1,1],[1,0,1],[1,1,1]])


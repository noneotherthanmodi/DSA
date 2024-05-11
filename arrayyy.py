#MAX SIZE OF AN ARRAY THAT CAN BE DEFINED INSIDE AN INT MAIN FUNC IS 10^6, AND GLOBALLY 10^7

# def larg_ele(arr:[int],n:int):
#     largest = arr[0]
#     for i in range(n):
#         if (arr[i]>largest):
#             largest = arr[i]
#     print(largest)
        


def larg_ele(arr:[int],n:int):
    arr.sort()
    print(arr)
    print(arr[-1])
        
larg_ele([7,2,1,5,2],5) 


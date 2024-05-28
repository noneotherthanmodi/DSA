# for i in range(4):
#     for j in range(4, i, -1):
#         print("*", end=" ")
#     print()

# asffas#
# Path: 2.PY TO COUNT NUMBER OF DIGITS
# from math import log10
# num = int(input("Enter a number: "))
# count = 0

# cnt = int(log10(num) + 1)
# print("The number of digits in the number are: ", cnt)

# while num > 0:
#     last_dig = num % 10
#     num = num//10
#     count += 1
    
# print("The number of digits in the number are: ", count)


# reverse of a number
#Write Your Code Here



# if __name__ == "__main__":
#     n = int(input("Enter a number:"))
#     reverse_dig = 0
#     while (n > 0) :
#         last_dig = n % 10 
#         reverse_dig = (reverse_dig*10) + last_dig 
#         n = n // 10
            
#     print(reverse_dig)


# PALINDROME
# n=int(input())  
# # taking n as a input 
# ## write your code !!
# reverse_dig = 0
# input_num = n
# while(n>0):
#     last_dig = n%10
#     reverse_dig = (reverse_dig*10) + last_dig
   
#     n = n//10

# if(reverse_dig == input_num):
#     print("true")
# else:
#     print("false")
    

# ARMSTRONG NUMBER
def checkArmstrong(n):
    #write your code here !!!!!!!!!
    palindrome_sum = 0
    original_num = n
    digit_count = len(str(n))
    while (n>0):
        last_dig = n%10
        palindrome_sum = palindrome_sum + (last_dig ** digit_count)
        n = n//10
    

    if palindrome_sum == original_num:
        print("true")
    else:
        print("false")
        
checkArmstrong(164)
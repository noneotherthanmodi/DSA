import time 
def countDigits(n: int) -> int:
    str_time = time.time()
    count = 0
    str_dig = str(n)
    for digit in str_dig:
        int_dig = int(digit)
        if int_dig!=0 and n%int_dig==0:
            count += 1
    end_time = time.time()
    final_time = end_time - str_time
    print(final_time)
    return count
print(countDigits(1234567890))
import math

def sqrt(number):
    if number < 1:
        return False
    
    start = 1
    end = number
    while (start <= end) : 
        mid = (start + end) // 2
          
        if (mid * mid == number) : 
            return mid 
              
        if (mid * mid < number) : 
            start = mid + 1
            ans = mid 
        else :  
            end = mid - 1
              
    return ans

print(sqrt(3)) # return 1
print(sqrt(0)) # return False
print(sqrt(626)) # return 25
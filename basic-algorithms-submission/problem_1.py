import math

def sqrt(number = 0):
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

print ("Pass" if  (3 == sqrt(9)) else "Fail") # Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail") # Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail") # Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail") # Pass
print ("Pass" if  (6 == sqrt(27)) else "Fail") # Fail
print ("Pass" if  (0 == sqrt(0)) else "Fail") # Fail
def get_min_max(ints):
    if len(ints) <= 0:
        return (0, 0)
    
    max = ints[0]
    min = ints[0]
    
    for i in range(0, len(ints)):
        if ints[i] > max:
            max = ints[i]
            
        if ints[i] < min:
            min = ints[i]
    
    return (min, max)


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail") #Pass
print ("Pass" if ((0, 9) == get_min_max([])) else "Fail") #Fail
print ("Pass" if ((-1, 100) == get_min_max([5, 4, 100, 6, 5, 12, 1, -1, 3, 4])) else "Fail") #Pass
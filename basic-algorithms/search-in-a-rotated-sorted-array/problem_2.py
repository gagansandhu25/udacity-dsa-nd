import math

def binary_search(input_list, number, low, high):
    l = low
    h = high
    mid = math.floor((l + h) / 2)
    
    if l > h:
        return -1
    
    if input_list[mid] == number:
        return mid
    
    if input_list[mid] > input_list[l]:
        if number >= input_list[l] and number < input_list[mid]:
            h = mid - 1
        else:
            l = mid + 1
            
        return binary_search(input_list, number, l, h)
    else:
        if number > input_list[mid] and number <= input_list[h]:
            l = mid + 1
        else:
            h = mid - 1
            
        return binary_search(input_list, number, l, h)
        
    return -1

def rotated_array_search(input_list, number):
    if len(input_list) <= 0:
        return -1
    
    return binary_search(input_list, number, 0, len(input_list) - 1)



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 1, 2, 3, 4], 8]) #Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) #Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) #Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8]) #Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1]) #Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) #Pass
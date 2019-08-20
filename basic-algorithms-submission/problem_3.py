def merge_sort(arr):
    if len(arr) > 1: 
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
  
        merge_sort(L)
        merge_sort(R)
  
        i = j = k = 0
          
        while i < len(L) and j < len(R): 
            if L[i] > R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

def rearrange_digits(input_list):
    if len(input_list) <= 0:
        return [0, 0]
    
    merge_sort(input_list)
    
    a = ""
    b = ""
    
    for i in range(0, len(input_list)):
        if i % 2 == 0:
            a += str(input_list[i])
        else:
            b += str(input_list[i]) 
   
    return [int(a), int(b)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]]) #Pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]]) #Pass
test_function([[6, 4, 3, 2, 7, 9, 9, 0, 1, 2], [97421, 96320]]) #Pass
test_function([[], [1, 2]]) #Fail
def swap(a, i1, i2):
    temp = a[i1]
    a[i1] = a[i2]
    a[i2] = temp

def sort_012(input_list):
    low = 0
    mid = 0
    high = len(input_list) - 1

    while mid <= high:
        if input_list[mid] == 0:
            swap(input_list, low, mid)
            low += 1
            mid += 1
        elif input_list[mid] == 2:
            swap(input_list, mid, high)
            high -= 1
        elif input_list[mid] == 1:
            mid += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]) #Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]) #Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) #Pass
# Naive method
# def hasArraywithSum(array, sum):
#   # loop over array and check if the sum matches
#   # if matches return True, if not return False
#   # [1, 2, 3, 4], sum = 3
#   for i in range(len(array)):
#     for j in range(len(array)-1):
#       if array[i] + array[j+1] == sum:
#         return True
#   return False

# Better method, assuing sorted
def hasArraywithSum(array, given_sum):
    # Add the start and end of the array and compare with sum
    # if the result is larger than the sum, move the right index to
    # the left by 1, if it is smaller, move the left index to the right by 1
    # [1, 2, 3, 4], sum = 3
    left_index = 0
    right_index = len(array) - 1

    for i in range(len(array)):
        array_sum = array[left_index] + array[right_index]
        if array_sum <= given_sum:
            left_index += 1
        elif array_sum >= given_sum:
            right_index += 1
        else:
            return True
    return False


print(hasArraywithSum([1, 2, 3, 4, 5, 7], 11))

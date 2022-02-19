## Merge sorted array
## Example input a = [1, 3, 4, 5, 16, 45] b =[1, 7, 34]
## Example output b = [1, 1, 3, 4, 5, 7, 16, 34, 45]

# Naive method
def merge_sorted_array_naive(a, b):
    #check input
    if len(a) == 0 or len(b) == 0:
        return a + b

    merged_array = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):

        if a[i] <= b[j]:
             merged_array.append(a[i])
             i+=1
        elif a[i] > b[j]:
            merged_array.append(b[j])
            j+=1

    return merged_array+a[i:]+b[j:]
    

# # Use bulid in function
# def merge_sorted_array(array1, array2):
#     new_list = array1 + array2
#     new_list.sort()
#     return new_list 4, 3

print(merge_sorted_array_naive([1, 3, 16, 45], [1, 7, 34]))

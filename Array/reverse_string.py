## reverse a string
# input: 'My Name is Chloe'
# output: 'eolhC si emaN yM'
  
#Naive O(n)
def reverse_string_On(string):
    # check input
    if len(string) < 2 or type(string) != str:
        return 'Please enter a string that has more than 1 char'
    # convert the string to a list

    total_items = len(string)-1
    new_list = []
    for i in range(len(string)):
        new_list.append(string[total_items-i])

    return ''.join(new_list)

# Use bulid-in method O(1)
def reverse_string_O1(string):
    if len(string) < 2 or type(string) != str:
        return 'Please enter a string that has more than 1 char'
    # convert the string to a list

    back_str = ''.join(list(reversed(list(string))))
    return back_str

# or just string[::-1]

print(reverse_string_On('My Name is Chloe'))
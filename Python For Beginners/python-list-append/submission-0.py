from typing import List # this is used to add type hints for List type

def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:
    my_list_length = len(my_list)
    elements_length = len(elements)
    tmp = [0] * (my_list_length + elements_length)

    for i in range(my_list_length):
        tmp[i] = my_list[i]
    
    for i in range(elements_length):
        tmp[i + my_list_length] = elements[i]
    
    return tmp

# do not modify below this line
print(append_to_list([1, 2, 3], [4, 5]))
print(append_to_list([], [1, 2, 3, 4]))

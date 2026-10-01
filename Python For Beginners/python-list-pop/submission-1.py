from typing import List # this is used to add type hints for List type

def remove_from_list(my_list: List[int], index: int) -> List[int]:
    for i in range(index, len(my_list)-1, 1):
        my_list[i] = my_list[i+1]
    
    return my_list[:-1]


def pop_n_from_list(my_list: List[int], n: int) -> List[int]:
    
    return my_list[:len(my_list)-n]


# don't modify below this line
print(remove_from_list([1, 2, 3, 4, 5], 2))
print(remove_from_list([1, 2, 3, 4, 5], 0))
print(remove_from_list([1, 2, 3, 4, 5], 4))

print(pop_n_from_list([1, 2, 3, 4, 5], 2))
print(pop_n_from_list([1, 2, 3, 4, 5], 0))
print(pop_n_from_list([1, 2, 3, 4, 5], 5))

from typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    arr1.extend(arr2)
    return arr1
  

def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    dic = {}
    res = []

    for num in arr1:
        dic[num] = dic.get(num, 0) + 1
    
    for num in arr2:
        if num in dic and dic[num] != 0:
            dic[num] -= 1
    
    for key, value in dic.items():
        if value != 0:
            res.append(key)
    
    return res


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))

from typing import List


def remove_element(arr: List[int], element: int) -> List[int]:
    res = arr[:]

    read = write = 0
    counts = 0

    while read < len(arr):
        if res[read] != element:
            res[write] = res[read]
            write += 1
            read += 1
        else:
            read += 1
            counts += 1
    
    for _ in range(counts):
        res.pop()

    return res


# do not modify below this line
arr = [1, 3, 5, 7, 9]

print(remove_element(arr, 3))
print(arr)
print(remove_element(arr, 9))
print(arr)
print(remove_element(arr, 1))
print(arr)

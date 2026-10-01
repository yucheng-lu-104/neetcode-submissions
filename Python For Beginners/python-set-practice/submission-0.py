from typing import List

def contains_duplicate(words: List[str]) -> bool:
    list_length = len(words)

    my_set = set(words)
    set_length = len(my_set)
    return list_length > set_length

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))

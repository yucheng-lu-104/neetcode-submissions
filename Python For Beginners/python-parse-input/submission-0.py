from typing import List

def read_integers() -> List[int]:
    user_input = input().split(",")
    
    for i in range(len(user_input)):
        user_input[i] = int(user_input[i])
    
    return user_input

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

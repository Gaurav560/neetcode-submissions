from typing import List

def read_integers() -> List[int]:
    num_string=input()
    char_list=num_string.split(",")

    int_list=[]
    for char in char_list:
        val=int(char)
        int_list.append(val)
    return int_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

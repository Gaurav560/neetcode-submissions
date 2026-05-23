def add_two_numbers() -> int:
    input_string=input()
    char_list=input_string.split(",")
    sum=0
    for char in char_list:
        val=int(char)
        sum+=val
    return sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

def add_two_numbers() -> int:
    user_input=input()
    nums=user_input.split(",")
    s=0
    for num in nums:
        s+=int(num)
    return s



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

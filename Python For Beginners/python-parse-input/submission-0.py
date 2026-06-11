from typing import List

def read_integers() -> List[int]:
    user_input=input()
    my_list=user_input.split(",")
    result_list=[]
    for i in my_list:
        result_list.append(int(i))
    return result_list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())

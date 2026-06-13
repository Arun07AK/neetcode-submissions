from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    arr_r=[]
    for i in range(len(arr)):
        arr_r.append(arr.pop())
    return arr_r


# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))

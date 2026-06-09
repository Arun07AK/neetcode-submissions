from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    s=0
    for i in nums:
        s+=i
    return s

def get_min(nums: List[int]) -> int:
    mi=nums[0]
    for i in nums:
        if i<mi:
            mi=i
    return mi

def get_max(nums: List[int]) -> int:
    ma=nums[0]
    for i in nums:
        if i>ma:
            ma=i
    return ma

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))

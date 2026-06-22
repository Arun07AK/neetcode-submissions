class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        longest=0
        for i in nums:
            if i-1 not in seen:
                l=1
                while( i+l in seen):
                    l+=1
                longest=max(l,longest)
        return longest
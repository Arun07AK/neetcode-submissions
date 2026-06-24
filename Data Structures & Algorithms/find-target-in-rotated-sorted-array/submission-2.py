class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        while l<=h:
            mid=(l+h)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[l] :#we have to use to info l and mid to chose btw right and left 
                if target>nums[mid] or target<nums[l]:# left
                    l=mid+1
                else:#right
                    h=mid-1
            else :#we have to use to info h and mid to chose btw right and left 
                if target<nums[mid] or target>nums[h]:#left
                    h=mid-1
                else:#right
                    l=mid+1
            
            
        return -1
        
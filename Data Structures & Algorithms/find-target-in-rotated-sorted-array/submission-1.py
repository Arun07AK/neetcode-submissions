class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        while l<=h:
            mid=(l+h)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[l] :#if the first part is sorted  
                if nums[l]<=target<nums[mid]: #check if target lies in this range
                    h=mid-1
                else:
                    l=mid+1
            else :#or else the target must lie in the second part 
                if nums[mid]<target<=nums[h]: #check if target lies in this range
                    l=mid+1
                else:
                    h=mid-1
            
            
        return -1
        